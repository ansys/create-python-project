from common import __version__


class TestVersion:
    @staticmethod
    def parse_version_number():
        version = {}
        with open("../src/_version.py") as fp:
            exec(fp.read(), version)
        return version

    def test_read(self):
        version = self.parse_version_number()
        assert '__version__' in version

    def test_import(self):
        version = self.parse_version_number()
        assert __version__ == version['__version__']
