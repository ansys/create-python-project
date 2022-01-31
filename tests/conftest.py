import pytest
from common import create_text_file_in_directory, ProjectGenerator


@pytest.fixture()
def destination_directory(tmp_path_factory):
    destination_path = tmp_path_factory.mktemp('destination')
    return destination_path


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
def generator(dummy_templates_path, destination_directory):
    return ProjectGenerator(destination_directory.parent, 'test_project',
                            templates_directory=dummy_templates_path)
