# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetRecommendationsResult',
    'AwaitableGetRecommendationsResult',
    'get_recommendations',
]

@pulumi.output_type
class GetRecommendationsResult:
    """
    A collection of values returned by getRecommendations.
    """
    def __init__(__self__, filter_by_categories=None, filter_by_resource_groups=None, id=None, recommendations=None):
        if filter_by_categories and not isinstance(filter_by_categories, list):
            raise TypeError("Expected argument 'filter_by_categories' to be a list")
        pulumi.set(__self__, "filter_by_categories", filter_by_categories)
        if filter_by_resource_groups and not isinstance(filter_by_resource_groups, list):
            raise TypeError("Expected argument 'filter_by_resource_groups' to be a list")
        pulumi.set(__self__, "filter_by_resource_groups", filter_by_resource_groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if recommendations and not isinstance(recommendations, list):
            raise TypeError("Expected argument 'recommendations' to be a list")
        pulumi.set(__self__, "recommendations", recommendations)

    @property
    @pulumi.getter(name="filterByCategories")
    def filter_by_categories(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "filter_by_categories")

    @property
    @pulumi.getter(name="filterByResourceGroups")
    def filter_by_resource_groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "filter_by_resource_groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def recommendations(self) -> Sequence['outputs.GetRecommendationsRecommendationResult']:
        """
        One or more `recommendations` blocks as defined below.
        """
        return pulumi.get(self, "recommendations")


class AwaitableGetRecommendationsResult(GetRecommendationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecommendationsResult(
            filter_by_categories=self.filter_by_categories,
            filter_by_resource_groups=self.filter_by_resource_groups,
            id=self.id,
            recommendations=self.recommendations)


def get_recommendations(filter_by_categories: Optional[Sequence[str]] = None,
                        filter_by_resource_groups: Optional[Sequence[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecommendationsResult:
    """
    Use this data source to access information about an existing Advisor Recommendations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.advisor.get_recommendations(filter_by_categories=[
            "security",
            "cost",
        ],
        filter_by_resource_groups=["example-resgroups"])
    pulumi.export("recommendations", example.recommendations)
    ```


    :param Sequence[str] filter_by_categories: Specifies a list of categories in which the Advisor Recommendations will be listed. Possible values are `HighAvailability`, `Security`, `Performance`, `Cost` and `OperationalExcellence`.
    :param Sequence[str] filter_by_resource_groups: Specifies a list of resource groups about which the Advisor Recommendations will be listed.
    """
    __args__ = dict()
    __args__['filterByCategories'] = filter_by_categories
    __args__['filterByResourceGroups'] = filter_by_resource_groups
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:advisor/getRecommendations:getRecommendations', __args__, opts=opts, typ=GetRecommendationsResult).value

    return AwaitableGetRecommendationsResult(
        filter_by_categories=__ret__.filter_by_categories,
        filter_by_resource_groups=__ret__.filter_by_resource_groups,
        id=__ret__.id,
        recommendations=__ret__.recommendations)
