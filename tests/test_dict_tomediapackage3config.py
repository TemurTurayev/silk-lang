"""
Tests for dict .toMediaPackage3Config() method - format dict as MediaPackage3 config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaPackage3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaPackage3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toMediaPackage3Config())')
        assert output[-1] == "host = localhost"

    def test_toMediaPackage3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toMediaPackage3Config())')
        assert output[-1] == "host = localhost\nport = 443"
