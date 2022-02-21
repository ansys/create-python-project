# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use,
# distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import pathlib
import shutil
import emoji
import coloredlogs
import logging
from dataclasses import dataclass
from string import Template
from typing import List
from .constants import DOT_FILES_TO_RENAME, GIT_RECC_LOG


os.environ['COLOREDLOGS_LOG_FORMAT'] = \
    '%(asctime)s [%(levelname)s] %(message)s'
os.environ['COLOREDLOGS_DATE_FORMAT'] = '%H:%M:%S'
os.environ['COLOREDLOGS_FIELD_STYLES'] = 'levelname=15; asctime=14'
os.environ['COLOREDLOGS_LEVEL_STYLES'] = \
    'info=35;debug=28;warning=202;error=14;error=background=red'
# Create a logger object.
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')
logger.setLevel(logging.INFO)
    

def copy_directory_and_contents_to_new_location(source: pathlib.Path,
                                                target: pathlib.Path, 
                                                just_files: bool = False) -> None:
    """Copies the source directory into the target directory.

    Ignores the `__pycache__` folder.

    :param source: an existing pathlib.Path to a directory
    :param target: target pathlib.Path directory. Does not have to exist yet.
    :param just_files: set True if only files should be copied to the new location.
    """
    logger.debug(f'Attempting to copy {source} to {target}')
    if just_files:
        logger.debug('Excluding directories from copy')
        for file in source.iterdir():
            if not file.is_dir():
                shutil.copy(file, target)
    else:
        shutil.copytree(source,
                        target, dirs_exist_ok=True, 
                        ignore=shutil.ignore_patterns("__pycache__"))


def add_project_name_to_files(files_with_template: List[pathlib.Path],
                              project_name: str):
    """Replaces all $project_name with project_name in all supplied files.

    Template-replacing function. Opens each file in turn and swaps all
    instances in the text of ``$project_name`` with the value of the
    parameter ``project_name``.

    :param files_with_template: List of files to be edited
    :param project_name: Name of the project to be inserted
    """
    for file in files_with_template:
        with open(file, 'r') as f:
            string = f.read()
        template = Template(string)
        result = template.substitute({'project_name': project_name})
        with open(file, 'w') as f:
            f.write(result)

    
def rename_files_in_directory(directory: pathlib.Path) -> None:
    """Rename specific files in a directory.

    This function will rename files as per the map in DOT_FILES_TO_RENAME.

    * 'flake8' -> '.flake8',
    * 'gitignore' -> '.gitignore',
    * 'gitattributes' -> '.gitattributes'}

    :param directory: pathlib.Path to the directory of files to be renamed.
    """
    logger.debug(f'Renaming files in {directory}')
    for file in os.listdir(directory):
        if file in DOT_FILES_TO_RENAME:
            logger.debug(f'--- renaming {directory / file} to '
                         f'{directory / DOT_FILES_TO_RENAME[file]}')
            os.rename(directory / file,
                      directory / DOT_FILES_TO_RENAME[file])


@dataclass
class ProjectTemplate:
    """Project template dataclass.

    ProjectTemplate has 2 properties:

    * `template_directory`
        - The pathlib.Path to the directory containing the template to be used.
    - `shared_files_directory`
        - The pathlib.Path to the directory with shared files across templates.

    """
    template_directory: pathlib.Path
    shared_files_directory: pathlib.Path
    cicd_type: str = 'github'


class ProjectTemplateAndDestinationChecker:
    """Provides capability to check validity of a
    supplied template and destination.

    Given a template and destination, this class provides
    the power to check the validity of both. Once initialised,
    the checks can be applied at a granular level or all at once
    using the `check()` method.

    :param template: pathlib.Path to the template directory
    :param destination: pathlib.Path to the destination directory
    """
    def __init__(self, template: ProjectTemplate, destination: pathlib.Path):
        """The template and destination must both be pathlib.Path objects."""
        self.template = template
        self.destination = destination

    def check_valid_template(self) -> None:
        """Checks the template is valid.

        Specifically checks that the template is

        - a directory
        - not called "shared" as this is reserved for the shared files folder

        """
        logger.debug(f'Checking that {self.template.template_directory} '
                     f'is a valid template')
        if not self.template.template_directory.is_dir():
            logger.error(f"Template {self.template.template_directory} "
                         f"is not a directory")
            raise NotADirectoryError('templates directory not a directory')
        elif self.template.template_directory.name == 'shared':
            logger.error(f"The 'shared' name is reserved and can not be used "
                         f"for a template. {self.template.template_directory} "
                         f"is named 'shared'")
            raise ValueError('template must not be called \'shared\'')
        logger.debug('confirmed')

    def check_valid_shared_directory(self) -> None:
        """Checks that the supplied shared directory is a directory.
        """
        logger.debug(f'Checking that {self.template.shared_files_directory} '
                     f'is a real directory')
        if not self.template.shared_files_directory.is_dir():
            logger.error(f"Template {self.template.shared_files_directory} "
                         f"is not a directory")
            raise NotADirectoryError('"shared" directory not a directory')
        logger.debug('confirmed')

    def check(self) -> None:
        """Performs all checks and raises errors when they fail."""
        self.check_valid_template()
        self.check_valid_shared_directory()
        self.check_destination_empty()

    def check_destination_empty(self) -> None:
        """Checks that the destination directory exists and is empty."""
        logger.debug(f'Checking that {self.destination} is currently empty')
        if self.destination.is_dir() and [d
                                          for d in self.destination.iterdir()]:
            error = f"Populated directory already exists at path " \
                    f"{self.destination}"
            logger.error(error)
            raise FileExistsError(error)


class ProjectGenerator:
    """Object that can create a project based on the supplied template.

    :param template: Template to generate the project from.
    """
    def __init__(self, template: ProjectTemplate):
        self.template = template

    def generate_template_at_destination(self,
                                         destination: pathlib.Path) -> None:
        """Creates the project at the supplied destination.

        :param destination: pathlib.Path to the empty destination directory.
        """
        ProjectTemplateAndDestinationChecker(self.template,
                                             destination).check()
        copy_directory_and_contents_to_new_location(
            self.template.template_directory,
            destination
        )
        if self.template.shared_files_directory is not None:
            copy_directory_and_contents_to_new_location(
              self.template.shared_files_directory,
              destination,
              just_files=True
            )
            if self.template.cicd_type == 'github':
                cicd_target = destination / '.github' / 'workflows'
                file_name = 'python-package.yml'
                cicd_source = self.template.shared_files_directory \
                              / 'cicd' / 'python-package.yml'
            else:
                cicd_target = destination
                file_name = 'azure-pipelines.yml'
                cicd_source = self.template.shared_files_directory \
                              / 'cicd' / 'azure-pipelines.yml'
            os.makedirs(cicd_target, exist_ok=True)
            shutil.copy(cicd_source, cicd_target / file_name)
        rename_files_in_directory(destination)

        logger.info(emoji.emojize('Project created successfully :thumbs_up:  '
                                  ':clapping_hands:'))

        print(GIT_RECC_LOG)

    def setup_documentation(self, destination: pathlib.Path) -> None:
        project_name = destination.name
        docs_dir = self.template.shared_files_directory / 'sphinxdoc'
        copy_directory_and_contents_to_new_location(docs_dir,
                                                    destination / 'doc')
        files_with_project_name = [
            destination / 'doc' / 'source' / 'conf.py',
            destination / 'doc' / 'source' / 'index.rst',
            destination / 'README.md'
        ]
        add_project_name_to_files(files_with_project_name, project_name)
