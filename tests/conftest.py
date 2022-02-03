import pytest
import pathlib
import os
from common import create_text_file_in_directory, \
    ProjectTemplate, get_builtin_templates_path, ProjectTemplateAndDestinationChecker


@pytest.fixture()
def destination_directory(tmp_path_factory):
    destination_path = tmp_path_factory.mktemp('destination')
    return destination_path


@pytest.fixture()
def builtin_templates_path():
    return get_builtin_templates_path()


@pytest.fixture()
def builtin_templates():
    templates_directory = get_builtin_templates_path()
    template_directories = [t for t in templates_directory.iterdir() if t.is_dir() and t.name != 'shared']
    templates = {t.name: ProjectTemplate(t, templates_directory / 'shared') for t in template_directories}
    return templates


@pytest.fixture()
def dummy_templates_path(tmp_path):
    templates_path = tmp_path / 'templates'
    templates_path.mkdir(parents=True)
    shared_path = templates_path / 'shared'
    shared_path.mkdir(parents=True)

    for name in ['README.md', 'README.rst', 'README.txt', '.dummy']:
        create_text_file_in_directory(templates_path, name)
    return templates_path


@pytest.fixture()
def preloaded_checker(destination_directory, builtin_templates_path):
    pt = ProjectTemplate(builtin_templates_path / 'classic', builtin_templates_path / 'shared')
    return ProjectTemplateAndDestinationChecker(pt, destination_directory)
