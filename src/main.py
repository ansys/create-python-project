# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use, distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import pathlib
import sys
from .generator import ProjectGenerator, ProjectTemplate
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
    templates_directory = get_builtin_templates_path()

    template = templates_directory / args.Template
    shared = templates_directory / 'shared'

    project_generator = ProjectGenerator(ProjectTemplate(template, shared))
    project_generator.generate_template_at_destination(root_folder / args.Name)
    return


def get_builtin_templates_path():
    return pathlib.Path(os.path.dirname(os.path.realpath(__file__))) / 'templates'


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--Name", help="Set the project name")
    parser.add_argument("-t", "--Template", help="Set the project template")
    return parser


if __name__ == '__main__':
    cli()




