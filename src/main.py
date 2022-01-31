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


def cli():
    if '--version' in sys.argv[1:]:
        print(__version__)
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--Name", help="Set the project name")
    parser.add_argument("-t", "--Template", help="Set the project template")
    args = parser.parse_args()

    project_generator = ProjectGenerator(pathlib.Path.cwd(), args.Name, args.Template)
    project_generator.generate()

    return


if __name__ == '__main__':
    if __debug__:
        pg = ProjectGenerator(pathlib.Path(tempfile.gettempdir()),
                              f'my-project-{ datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}', 'classic')
        pg.generate()
    else:
        cli()




