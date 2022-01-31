from common import get_templates, create_x_many_templates, \
    copy_template, create_one_template, generate_project_folder, \
    create_text_file_in_directory, replace_word_in_file
import pathlib
import pytest
import datetime


class TestGetTemplates:
    def test_correct_number_returned(self, dummy_templates_path):
        create_x_many_templates(dummy_templates_path, 5)
        results = get_templates(dummy_templates_path)
        assert len(results) == 5

    def test_only_returns_directories(self, dummy_templates_path):
        create_x_many_templates(dummy_templates_path, 5)
        results = get_templates(dummy_templates_path)
        for r in results:
            assert r.is_dir()

    def test_raises_error_when_not_directory(self, dummy_templates_path):
        with pytest.raises(NotADirectoryError):
            get_templates(pathlib.Path(dummy_templates_path / 'README.txt'))


class TestCopyTemplate:
    def test_simple_copy(self, dummy_templates_path, destination_directory):
        name = f'my_new_template{datetime.datetime.now().microsecond}'
        create_one_template(dummy_templates_path, name)
        result = copy_template(dummy_templates_path, name, destination_directory)
        assert result is None


class TestGenerateProjectFolder:
    @pytest.mark.parametrize('template', ['classic', 'gRPC-api', 'package', 'rest-api'])
    def test_internal_templates(self, dummy_templates_path, destination_directory, template):
        generate_project_folder(destination_directory, 'my_project', template)

    def test_shared_template_fails(self, dummy_templates_path, destination_directory):
        with pytest.raises(ValueError):
            generate_project_folder(destination_directory, 'my_project', 'shared')

    def test_nonsense_template_fails(self, dummy_templates_path, destination_directory):
        with pytest.raises(ValueError):
            generate_project_folder(destination_directory, 'my_project', 'this definitely does not exist')


class TestReplaceWordInFile:
    @pytest.mark.parametrize('word', ['oxygen', 'word and spaces', '(.punctuation!?)'])
    def test_simple_replace(self, destination_directory, word):
        create_text_file_in_directory(destination_directory, 'test.txt')
        replace_word_in_file(destination_directory / 'test.txt', 'test.txt', word)
        with open(destination_directory / 'test.txt', 'r') as f:
            result = f.readline()
            assert word in result
