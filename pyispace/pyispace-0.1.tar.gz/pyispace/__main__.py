import argparse
import json
from pathlib import Path

import pandas as pd

from pyispace import train_is
from pyispace.utils import scriptcsv


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyISpace - Python Instance Space Analysis toolkit.")
    parser.add_argument('-r', '--rootdir', dest='rootdir', default=None, required=False, metavar='FILE',
                        help="rootdir path")
    args = parser.parse_args()

    if args.rootdir is not None:
        rootdir = Path(args.rootdir)
        if not rootdir.exists():
            raise NotADirectoryError(f"Invalid directory {repr(args.rootdir)}.")
    else:
        rootdir = Path().absolute()

    opts_path = rootdir / 'options.json'
    if opts_path.is_file():
        with open(opts_path) as f:
            opts = json.load(f)
    else:
        raise FileNotFoundError(f"File 'options.json' not found in specified path {repr(str(rootdir))}.")

    meta_path = rootdir / 'metadata.csv'
    if meta_path.is_file():
        metadata = pd.read_csv(meta_path, index_col='instances')
    else:
        raise FileNotFoundError(f"File 'metadata.csv' not found in specified path {repr(str(rootdir))}.")

    out = train_is(metadata, opts)
    scriptcsv(out, rootdir)
