# Copyright (c) 2022 Ansys, Inc. and its affiliates.
# Unauthorised use, distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import pathlib
import sys
import argparse
from .generator import ProjectGenerator, ProjectTemplate
from ._version import __version__


def parse_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Parse command line arguments and flag up issues with them.

    :param parser: argparse.ArgumentParser object
    :return: arguments namespace
    """
    args = parser.parse_args(sys.argv[1:])
    if args.templates is True:
        path = get_builtin_templates_path()
        available_templates = [p.name
                               for p in path.iterdir() if p.name != 'shared']
        print('Available templates are:')
        for template in available_templates:
            print(f' * {template}')
        sys.exit()
    if args.Name is None:
        print('No project name supplied')
        parser.print_help()
        sys.exit()
    return args


def cli(root_folder: pathlib.Path = None) -> None:
    """Command Line Interface function.

    Constructs the CLI and executes the program itself.
    The root folder is the one in which the project
    should be created. This defaults to the current working
    directory but can be set to be something else. This
    functionality exists primarily for testing purposes.

    :param root_folder: Directory in which to create the project directory
    """
    args = parse_args(create_parser())
    if root_folder is None:
        root_folder = pathlib.Path.cwd()
    templates_directory = get_builtin_templates_path()

    template = templates_directory / args.Template
    shared = templates_directory / 'shared'

    project_generator = ProjectGenerator(ProjectTemplate(template, shared, args.cicd.lower()))
    project_generator.generate_template_at_destination(root_folder / args.Name)
    project_generator.setup_documentation(root_folder / args.Name)
    return


def get_builtin_templates_path() -> pathlib.Path:
    """Return the pathlib.Path to the package's builtin templates

    :return: template pathlib.Path
    """
    return pathlib.Path(
        os.path.dirname(os.path.realpath(__file__))
    ) / 'templates'


def create_parser() -> argparse.ArgumentParser:
    """Construct the parser for the CLI.

    Adds arguments to the parser but does not parse the arguments itself.

    :return: argparse.ArgumentParser instance
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",
                        "--Name",
                        help="Set the project name. "
                             "This is a required argument.")
    parser.add_argument("-t",
                        "--Template",
                        help="Set the project template. "
                             "Defaults to 'classic'.",
                        default='classic',
                        required=False)
    parser.add_argument('--templates',
                        help='View all the available project templates.',
                        action='store_true',
                        default=False,
                        required=False)
    parser.add_argument('--version',
                        action='version',
                        version=f'ansys-create-python-project {__version__}')
    parser.add_argument('--cicd',
                        help="Github Actions (github) or Azure Pipelines (ado)?",
                        default='github',
                        required=False)

    return parser


if __name__ == '__main__':
    cli()




