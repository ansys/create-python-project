# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use, distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import pathlib
import shutil
import emoji
import coloredlogs
import logging
from dataclasses import dataclass
from .constants import Colors, DOT_FILES_TO_RENAME, GIT_RECC_LOG


os.environ['COLOREDLOGS_LOG_FORMAT'] = '%(asctime)s [%(levelname)s] %(message)s'
os.environ['COLOREDLOGS_DATE_FORMAT'] = '%H:%M:%S'
os.environ['COLOREDLOGS_FIELD_STYLES'] = 'levelname=15; asctime=14'
os.environ['COLOREDLOGS_LEVEL_STYLES'] = 'info=35;debug=28;warning=202;error=14;error=background=red'
# Create a logger object.
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')
logger.setLevel(logging.INFO)
    

def copy_directory_and_contents_to_new_location(source: pathlib.Path, target: pathlib.Path):
    logger.debug(f'Attempting to copy {source} to {target}')
    shutil.copytree(source, target, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"))
    
    
def rename_files_in_directory(directory: pathlib.Path):
    logger.debug(f'Renaming files in {directory}')
    for file in os.listdir(directory):
        if file in DOT_FILES_TO_RENAME:
            logger.debug(f'--- renaming {directory / file} to {directory / DOT_FILES_TO_RENAME[file]}')
            os.rename(directory / file,
                      directory / DOT_FILES_TO_RENAME[file])


@dataclass
class ProjectTemplate:
    template_directory: pathlib.Path
    shared_files_directory: pathlib.Path


class ProjectTemplateAndDestinationChecker:
    def __init__(self, template: ProjectTemplate, destination: pathlib.Path):
        self.template = template
        self.destination = destination

    def check_valid_template(self):
        logger.debug(f'Checking that {self.template.template_directory} is a valid template')
        if not self.template.template_directory.is_dir():
            logger.error(f"Template {self.template.template_directory} is not a directory")
            raise NotADirectoryError('templates directory not a directory')
        elif self.template.template_directory.name == 'shared':
            logger.error(f"The 'shared' name is reserved and can not be used for a template. "
                         f"{self.template.template_directory} is named 'shared'")
            raise ValueError('template must not be called \'shared\'')
        logger.debug('confirmed')

    def check_valid_shared_directory(self):
        logger.debug(f'Checking that {self.template.shared_files_directory} is a real directory')
        if not self.template.shared_files_directory.is_dir():
            logger.error(f"Template {self.template.shared_files_directory} is not a directory")
            raise NotADirectoryError('"shared" directory not a directory')
        logger.debug('confirmed')

    def check(self):
        self.check_valid_template()
        self.check_valid_shared_directory()
        self.check_destination_empty()

    def check_destination_empty(self):
        logger.debug(f'Checking that {self.destination} is currently empty')
        if self.destination.is_dir() and [d for d in self.destination.iterdir()]:
            error = f"Populated directory already exists at path {self.destination}"
            logger.error(error)
            raise FileExistsError(error)


class ProjectGenerator:
    def __init__(self, template: ProjectTemplate):
        self.template = template

    def generate_template_at_destination(self, destination: pathlib.Path):
        ProjectTemplateAndDestinationChecker(self.template, destination).check()
        copy_directory_and_contents_to_new_location(self.template.template_directory, destination)
        if self.template.shared_files_directory is not None:
            copy_directory_and_contents_to_new_location(self.template.shared_files_directory, destination)
        rename_files_in_directory(destination)

        logger.info(emoji.emojize('Project created successfully :thumbs_up:  :clapping_hands:'))

        print(GIT_RECC_LOG)
