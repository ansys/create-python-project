from common import create_x_many_templates, create_one_template, \
    create_text_file_in_directory, replace_word_in_file, ProjectGenerator
import pytest
import datetime


class TestGetTemplates:
    def test_correct_number_returned(self, destination_directory, dummy_templates_path):
        generator = ProjectGenerator(destination_directory.parent, 'test_project',
                                     templates_directory=dummy_templates_path)
        create_x_many_templates(generator.templates_directory, 5)
        results = generator.get_templates()
        assert len(results) == 5

    def test_only_returns_directories(self, destination_directory, dummy_templates_path):
        generator = ProjectGenerator(destination_directory.parent, 'test_project',
                                     templates_directory=dummy_templates_path)
        create_x_many_templates(generator.templates_directory, 5)
        results = generator.get_templates()
        for r in results:
            assert (dummy_templates_path / r).is_dir()

    def test_raises_error_when_not_directory(self, destination_directory, dummy_templates_path):
        generator = ProjectGenerator(destination_directory.parent, 'test_project',
                                     templates_directory=dummy_templates_path / 'README.txt')
        with pytest.raises(NotADirectoryError):
            generator.get_templates()


class TestCopyTemplate:
    def test_simple_copy(self, destination_directory, dummy_templates_path):
        name = f'my_new_template{datetime.datetime.now().microsecond}'
        generator = ProjectGenerator(destination_directory.parent, 'test_project',
                                     templates_directory=dummy_templates_path,
                                     selected_template=name)
        create_one_template(dummy_templates_path, name)
        result = generator.copy_template()  # dummy_templates_path, name, destination_directory)
        assert result is None


class TestGenerateProjectFolder:
    @pytest.mark.parametrize('template', ['classic', 'gRPC-api', 'package', 'rest-api'])
    def test_internal_templates(self, destination_directory, template):
        pg = ProjectGenerator(destination_directory, 'test_proj', template)
        pg.generate()

    def test_shared_template_fails(self, destination_directory):
        with pytest.raises(ValueError):
            pg = ProjectGenerator(destination_directory, 'test_proj', 'shared')
            pg.generate()

    def test_nonsense_template_fails(self, destination_directory):
        with pytest.raises(ValueError):
            pg = ProjectGenerator(destination_directory, 'test_proj', 'bogus template')
            pg.generate()


class TestReplaceWordInFile:
    @pytest.mark.parametrize('word', ['oxygen', 'word and spaces', '(.punctuation!?)'])
    def test_simple_replace(self, destination_directory, word):
        create_text_file_in_directory(destination_directory, 'test.txt')
        replace_word_in_file(destination_directory / 'test.txt', 'test.txt', word)
        with open(destination_directory / 'test.txt', 'r') as f:
            result = f.readline()
            assert word in result
