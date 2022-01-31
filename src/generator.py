# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use, distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import pathlib
import subprocess
import shutil
import emoji
import coloredlogs
import logging
from easygui import *

os.environ['COLOREDLOGS_LOG_FORMAT'] = '%(asctime)s [%(levelname)s] %(message)s'
os.environ['COLOREDLOGS_DATE_FORMAT'] = '%H:%M:%S'
os.environ['COLOREDLOGS_FIELD_STYLES'] = 'levelname=15; asctime=14'
os.environ['COLOREDLOGS_LEVEL_STYLES'] = 'info=35;debug=28;warning=202;error=14;error=background=red'
# Create a logger object.
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

dot_files_to_rename = {'flake8': '.flake8',
                       'gitignore': '.gitignore',
                       'gitattributes': '.gitattributes'}


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def has_pipx():
    try:
        subprocess.run(["pipx", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logger.info("pipx installed")
        return True
    except:
        logger.error("pipx is not installed. Follow these instructions https://pypa.github.io/pipx/installation/")
        return False


def replace_word_in_file(filepath, word_to_replace, new_value):
    with open(filepath) as file:
        input_data = file.read()
        input_data = input_data.replace(word_to_replace, new_value)
        file.close()
        with open(filepath, 'w') as new_file:
            new_file.write(input_data)


class ProjectGenerator:
    def __init__(self, root_directory: pathlib.Path, project_name: str,
                 selected_template: str = 'classic', templates_directory: pathlib.Path = None):
        self.root = root_directory
        self.project = project_name
        self.destination = self.root / self.project
        self._selected_template = selected_template
        self._templates_directory = templates_directory

    @property
    def selected_template(self):
        self.check_valid_selected_template()
        return self._selected_template
        
    @property
    def templates_directory(self):
        if self._templates_directory is None:
            self._templates_directory = pathlib.Path(os.path.dirname(os.path.realpath(__file__))) / 'templates'
        return self._templates_directory

    @property
    def templates(self):
        return self.get_templates()

    def get_templates(self):
        if not self.templates_directory.is_dir():
            logger.error("Templates not found")
            raise NotADirectoryError('templates directory not found')
        else:
            templates = self.templates_directory.glob('*')
        return [x.name for x in templates if x.is_dir() and x.name != 'shared' and not x.name.startswith('.')]

    def copy_template(self):
        # Copy template resources
        template_directory = self.templates_directory / self.selected_template
        shutil.copytree(template_directory, self.destination, dirs_exist_ok=True)

        # Copy shared resources
        shared_directory = self.templates_directory / 'shared'
        shutil.copytree(shared_directory, self.destination, dirs_exist_ok=True)

    def generate(self):
        logger.info(f'Attempting to copy {self.selected_template} to {self.destination}')
        self.check_destination_directory_empty()
        self.copy_template_and_rename_files()

        logger.info(f"{Colors.BOLD}The {self.project} project has been initialized successfully "
                    f"based on {self.selected_template} template!{Colors.BOLD}")
        message = f"""{Colors.OKCYAN}We recommend you track your project using git 
        and store it in a remote repository, such as on ADO or GitHub. 
        This can be done by following these instructions provided you already have git installed.
            1- Navigate to the created project directory on the command line ./{self.project} 
            2- Make the directory into a git repo and link it to a remote origin (GitHub/ADO/etc.)
                2.1 [Optional] -  git init
                2.2 [Optional] -  git remote add origin <git_repository_url>
                2.3 [Optional] -  git add . && git commit -m \"initial commit\"
                2.4 [Optional] -  git push origin main {Colors.OKCYAN} 
    
        {Colors.WARNING}:collision: :star-struck: :star-struck: :star-struck: :star-struck: :collision:{Colors.WARNING}
        """
        print(emoji.emojize(message))
        logger.info(emoji.emojize('Success :thumbs_up:  :clapping_hands:'))
        return

    def check_valid_selected_template(self):
        if self._selected_template in self.templates:
            return
        else:
            self.raise_error_for_unavailable_template()

    def raise_error_for_unavailable_template(self):
        if self._selected_template == 'shared':
            error = "'shared' is a reserved directory and can not be used as a template name."
        else:
            error = f"Selected template \"{self._selected_template}\" not available."
        logger.error(error)
        logger.info("Available templates:")
        print(self.templates)
        raise ValueError(error)

    def copy_template_and_rename_files(self):
        self.copy_template()
        for file in os.listdir(self.destination):
            if file in dot_files_to_rename:
                os.rename(self.destination / file,
                          self.destination / dot_files_to_rename[file])

    def check_destination_directory_empty(self):
        if self.destination.is_dir() and [d for d in self.destination.iterdir()]:
            error = f"Populated directory already exists at path {self.destination}"
            logger.error(error)
            raise FileExistsError(error)


