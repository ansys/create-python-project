import pytest

from common import __version__


class TestVersion:

    def test_basic(self):
        assert __version__ is not None

    @staticmethod
    def parse_version_number():
        version = {}
        with open("../src/_version.py") as fp:
            exec(fp.read(), version)
        return version
