import logging
import math
import time
from dataclasses import dataclass
from itertools import repeat
from multiprocessing import Pool, cpu_count
from typing import List, Union

import numpy as np
import pandas as pd
from scipy.spatial import Delaunay
from scipy.special import gamma
from shapely import geometry
from shapely.ops import cascaded_union, polygonize, triangulate, unary_union
from sklearn.cluster import DBSCAN

_required_opts = ['PI']
_logger = logging.getLogger(__name__)


@dataclass
class FootprintOutput:
    polygon: geometry.MultiPolygon
    area: float
    elements: int
    good_elements: int
    density: float
    purity: float


# _empty_footprint = FootprintOutput(geometry.MultiPolygon(), 0, 0, 0, 0, 0)
def _empty_footprint() -> FootprintOutput:
    return FootprintOutput(geometry.MultiPolygon(), 0, 0, 0, 0, 0)


def _copy_footprint(obj: FootprintOutput) -> FootprintOutput:
    return FootprintOutput(**obj.__dict__)


@dataclass
class TraceOutput:
    space: FootprintOutput
    good: List[FootprintOutput]
    best: List[FootprintOutput]
    summary: pd.DataFrame


class TraceException(Exception):
    def __init__(self):
        super().__init__("There are not enough instances to calculate a footprint. "
                         "The subset of instances used is too small.")


def alpha_shape(points: np.ndarray, alpha=1.0):
    """
    Compute the alpha shape (concave hull) of a set of points.

    :param points: array of points (x,y)
    :param float alpha: alpha value to influence the gooeyness of the border. Smaller numbers don't fall inward as much
        as larger numbers. Too large, and you lose everything!
    """
    if len(points) < 3:
        # When you have a triangle, there is no sense
        # in computing an alpha shape.
        return geometry.MultiPoint(list(points)).convex_hull, points
    elif len(points) == 3:
        return geometry.Polygon(points), points

    # coords = np.array([point.coords[0] for point in points])
    tri = Delaunay(points)
    triangles = points[tri.simplices]
    a = ((triangles[:, 0, 0] - triangles[:, 1, 0]) ** 2 + (triangles[:, 0, 1] - triangles[:, 1, 1]) ** 2) ** 0.5
    b = ((triangles[:, 1, 0] - triangles[:, 2, 0]) ** 2 + (triangles[:, 1, 1] - triangles[:, 2, 1]) ** 2) ** 0.5
    c = ((triangles[:, 2, 0] - triangles[:, 0, 0]) ** 2 + (triangles[:, 2, 1] - triangles[:, 0, 1]) ** 2) ** 0.5
    s = (a + b + c) / 2.0
    areas = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    circums = a * b * c / (4.0 * areas)
    filtered = triangles[circums < (1.0 / alpha)]
    edge1 = filtered[:, (0, 1)]
    edge2 = filtered[:, (1, 2)]
    edge3 = filtered[:, (2, 0)]
    edge_points = np.unique(np.concatenate((edge1, edge2, edge3)), axis=0).tolist()
    m = geometry.MultiLineString(edge_points)
    triangles = list(polygonize(m))
    return cascaded_union(triangles), edge_points


def count_points(pts):
    if pts.is_empty:
        return 0
    elif pts.type == 'Point':
        return 1
    elif pts.type == 'MultiPoint':
        return len(pts)
    else:
        raise TypeError


def inner_intersection(poly, pts):
    intersec = poly.intersection(pts)
    intersec_bound = poly.boundary.intersection(intersec)
    return intersec.difference(intersec_bound)


def copy_polygon(poly: Union[geometry.Polygon, geometry.MultiPolygon]):
    return poly.__class__(poly)


def estimate_epsilon(x, k):
    m, n = np.shape(x)
    eps = ((np.prod(x.max(axis=0) - x.min(axis=0)) * k * gamma(.5 * n + 1)) / (m * np.sqrt(np.pi ** n))) ** (1 / n)
    return eps


def make_summary(space: FootprintOutput, good: List[FootprintOutput], best: List[FootprintOutput], algolabels: List):
    assert len(good) == len(best)
    cols = ['Area_Good_Normalized', 'Density_Good_Normalized', 'Purity_Good',
            'Area_Best_Normalized', 'Density_Best_Normalized', 'Purity_Best']
    rows = []
    for i in range(len(good)):
        rows.append([good[i].area / space.area,
                     good[i].density / space.density,
                     good[i].purity,
                     best[i].area / space.area,
                     best[i].density / space.density,
                     best[i].purity]
                    )
    summary = pd.DataFrame(rows, index=pd.Index(algolabels, name='Row'), columns=cols)
    return summary


def trace(Z: np.ndarray, Ybin: np.ndarray, P: np.ndarray, beta: np.ndarray, algolabels: list, parallel=True, **kwargs):
    _logger.info("TRACE is calculating the space area and density.")
    ninst = Z.shape[0]
    nalgos = Ybin.shape[1]
    space = trace_build(Z, np.ones(ninst, dtype=bool), kwargs['PI'])
    _logger.debug(f"Space area: {space.area}")
    _logger.debug(f"Space density: {space.density}")

    _logger.info("TRACE is calculating the algorithm footprints.")
    if parallel:
        _logger.warning("Some log messages are temporarily disabled in parallel mode. This functionality will be added "
                        "in future versions")
        with Pool(processes=cpu_count()) as pool:
            _logger.info(f"Calculating footprints...")
            good = pool.starmap_async(trace_build_wrapper,
                                      zip(repeat(Z), (Ybin[:, i] for i in range(nalgos)), repeat(kwargs['PI'])))
            best = pool.starmap_async(trace_build_wrapper,
                                      zip(repeat(Z), (P == i for i in range(nalgos)), repeat(kwargs['PI'])))
            good = good.get()
            best = best.get()
    else:
        good = []
        best = []
        for i in range(nalgos):
            start = time.time()
            _logger.info(f"Good performance footprint for {repr(algolabels[i])}")
            try:
                good.append(trace_build(Z, Ybin[:, i], kwargs['PI']))
            except TraceException as e:
                good.append(_empty_footprint())
                _logger.warning(str(e))

            _logger.info(f"Best performance footprint for {repr(algolabels[i])}")
            try:
                best.append(trace_build(Z, P == i, kwargs['PI']))
            except TraceException as e:
                good.append(_empty_footprint())
                _logger.warning(str(e))

            end = time.time()
            _logger.debug(f"Algorithm {repr(algolabels[i])} completed. Elapsed time: {(end - start):.2f} s")

    _logger.info("TRACE is detecting and removing contradictory sections of the footprints.")
    for i in range(nalgos - 1):
        _logger.debug(f"Base algorithm {repr(algolabels[i])}")
        for j in range(i + 1, nalgos):
            _logger.debug(f"TRACE is comparing {repr(algolabels[i])} with {repr(algolabels[j])}")
            best[i], best[j] = trace_contra(best[i], best[j], Z, P == i, P == j)
            _logger.debug(f"Test algorithm {repr(algolabels[j])} completed.")
        _logger.debug(f"Base algorithm {repr(algolabels[i])} completed.")

    _logger.info("TRACE is removing tiny areas, which are smaller than 0.1% of the space area.")
    for i in range(nalgos):
        good[i] = remove_tiny_areas(good[i], 0.001 * space.area, Z, Ybin[:, i])
        best[i] = remove_tiny_areas(best[i], 0.001 * space.area, Z, P == i)

    summary = make_summary(space, good, best, algolabels)
    _logger.info("TRACE has completed.")
    return TraceOutput(space, good, best, summary)


def trace_build_wrapper(*args):
    try:
        return trace_build(*args)
    except TraceException:
        return FootprintOutput(geometry.MultiPolygon(), 0, 0, 0, 0, 0)


def trace_build(Z, Ybin, PI):
    Ig = np.unique(Z[Ybin, :], axis=0)
    if Ig.shape[0] < 3:
        raise TraceException

    nn = max(math.ceil(0.01 * sum(Ybin)), 2)
    eps = estimate_epsilon(Ig, nn)
    clustering = DBSCAN(eps=eps, min_samples=nn).fit(Ig)
    polygon = geometry.Polygon()
    for i in range(np.max(clustering.labels_) + 1):
        polydata = Ig[clustering.labels_ == i, :]
        if polydata.shape[0] < 3:
            continue
        concave_hull, edge_points = alpha_shape(polydata, alpha=0.5)
        boundary = np.array(concave_hull.exterior.xy).T
        aux = trace_fitpoly(boundary, Z, Ybin, PI)
        if not aux.is_empty:
            polygon = polygon.union(aux)

    if not polygon.is_empty:
        area = polygon.area
        elements = count_points(polygon.intersection(geometry.MultiPoint(Z)))
        good_elements = count_points(polygon.intersection(geometry.MultiPoint(Z[Ybin, :])))
        density = elements / area
        purity = good_elements / elements
        return FootprintOutput(polygon, area, elements, good_elements, density, purity)
    else:
        raise TraceException


def trace_contra(base: FootprintOutput, test: FootprintOutput, Z: np.ndarray, Ybase: np.ndarray, Ytest: np.ndarray):
    if base.polygon.is_empty or test.polygon.is_empty:
        return base, test

    def degenerate(p):
        if not (isinstance(p, geometry.Polygon) or isinstance(p, geometry.MultiPolygon)):
            return True
        else:
            return False

    base = _copy_footprint(base)
    base.polygon = copy_polygon(base.polygon)
    test = _copy_footprint(test)
    test.polygon = copy_polygon(test.polygon)

    z_points = geometry.MultiPoint(Z)
    z_base = geometry.MultiPoint(Z[Ybase, :])
    z_test = geometry.MultiPoint(Z[Ytest, :])
    contradiction = base.polygon.intersection(test.polygon)

    while not contradiction.is_empty:
        n_elements = count_points(contradiction.intersection(z_points))
        if n_elements == 0:
            break
        n_good_elements_base = count_points(contradiction.intersection(z_base))
        n_good_elements_test = count_points(contradiction.intersection(z_test))
        purity_base = n_good_elements_base / n_elements
        purity_test = n_good_elements_test / n_elements

        if purity_base > purity_test:
            test.polygon = test.polygon.difference(contradiction)
        elif purity_test > purity_base:
            base.polygon = base.polygon.difference(contradiction)
        else:
            break
        if base.polygon.is_empty or test.polygon.is_empty:
            break
        else:
            contradiction = base.polygon.intersection(test.polygon)
            if degenerate(contradiction):
                break

    if base.polygon.is_empty:
        base = _empty_footprint()
    else:
        base.area = base.polygon.area
        base.elements = count_points(base.polygon.intersection(z_points))
        base.good_elements = count_points(base.polygon.intersection(z_base))
        base.density = base.elements / base.area
        base.purity = base.good_elements / base.elements
    if test.polygon.is_empty:
        test = _empty_footprint()
    else:
        test.area = test.polygon.area
        test.elements = count_points(test.polygon.intersection(z_points))
        test.good_elements = count_points(test.polygon.intersection(z_base))
        test.density = test.elements / test.area
        test.purity = test.good_elements / test.elements

    return base, test


def remove_tiny_areas(footprint: FootprintOutput, threshold: float, Z: np.ndarray, Ybin: np.ndarray) -> FootprintOutput:
    """
    Eliminates tiny parts of a MultiPolygon (or Polygon).

    :param FootprintOutput footprint: footprint struct object
    :param float threshold: small area reference value
    :param np.ndarray Z: IS coordinates
    :param np.ndarray Ybin: binarized response variable
    """
    poly = footprint.polygon
    z_points = geometry.MultiPoint(Z)
    z_good = geometry.MultiPoint(Z[Ybin, :])

    if poly.area < threshold:
        return _empty_footprint()
    elif isinstance(poly, geometry.Polygon):
        return footprint
    elif isinstance(poly, geometry.MultiPolygon):
        poly_list = [p for p in poly if p.area > threshold]
        if len(poly_list) == 0:
            return _empty_footprint()
        elif len(poly_list) == 1:
            polygon = poly_list[0]
        else:
            polygon = geometry.MultiPolygon(poly_list)
        area = polygon.area
        elements = count_points(polygon.intersection(z_points))
        good_elements = count_points(polygon.intersection(z_good))
        density = elements / area
        purity = good_elements / elements
        return FootprintOutput(polygon, area, elements, good_elements, density, purity)
    else:
        raise TypeError("Accepts only Polygon or MultiPolygon as input.")


def trace_tight(polygon, Z, Ybin, *args, **kwargs):
    pass


def trace_fitpoly(polydata: np.ndarray, Z: np.ndarray, Ybin: np.ndarray, PI):
    if Ybin.dtype != bool:
        raise TypeError("Ybin must be an array of bools.")
    if polydata.shape[0] < 3:
        return geometry.Polygon()

    triangles = triangulate(geometry.MultiPoint(polydata))
    if ~Ybin.all():
        z_points = geometry.MultiPoint(Z)
        good_points = geometry.MultiPoint(Z[Ybin])
        if len(triangles) == 0:
            return geometry.Polygon()

        keep = []
        for tri in triangles:
            # n_elements = count_points(inner_intersection(tri, z_points))
            # n_good_elements = count_points(inner_intersection(tri, good_points))
            n_elements = count_points(tri.intersection(z_points))
            n_good_elements = count_points(tri.intersection(good_points))

            if n_elements > 0:
                if (n_good_elements / n_elements) < PI:
                    continue
                else:
                    keep.append(tri)
        return unary_union(keep)
    else:
        return unary_union(triangles)
