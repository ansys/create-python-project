from common import cli, create_parser
import pytest
import sys


class TestCLI:
    @pytest.mark.parametrize('flags', [[], ['--Name', 'thing'], ['--Template', 'classic']])
    def test_version(self, flags):
        sys.argv = ['', '--version']
        sys.argv.extend(flags)
        assert cli() is None

    @pytest.mark.parametrize('template', ['classic', 'package', 'gRPC-api', 'rest-api'])
    def test_generate_projects(self, template, destination_directory):
        sys.argv = ['', '--Name', 'my_proj', '--Template', template]
        cli(root_folder=destination_directory)


class TestCreateParser:
    @pytest.mark.parametrize('flag', ['--Name', '-n'])
    def test_name(self, flag):
        sys.argv = ['', flag, 'my_proj']
        parser = create_parser()
        assert parser.parse_args().Name == 'my_proj'

    @pytest.mark.parametrize('flag', ['--Template', '-t'])
    def test_template(self, flag):
        sys.argv = ['', flag, 'classic']
        parser = create_parser()
        assert parser.parse_args().Template == 'classic'
