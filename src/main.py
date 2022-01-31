# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use, distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import pathlib
import sys
import tempfile
from datetime import datetime
from src.generator import ProjectGenerator
import argparse

__version__ = '0.0.11'


def cli(root_folder=None):
    if '--version' in sys.argv[1:]:
        print(__version__)
        return
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    if root_folder is None:
        root_folder = pathlib.Path.cwd()
    pg = ProjectGenerator(root_folder, args.Name, selected_template=args.Template)
    pg.generate()
    return


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--Name", help="Set the project name")
    parser.add_argument("-t", "--Template", help="Set the project template")
    return parser


if __name__ == '__main__':
    if __debug__:
        pg = ProjectGenerator(pathlib.Path(tempfile.gettempdir()),
                              f'my-project-{ datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}', 'classic')
        pg.generate()
    else:
        cli()




