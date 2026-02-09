"""
Tests for dict .toMediaConvert3Config() method - format dict as MediaConvert3 config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaConvert3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaConvert3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toMediaConvert3Config())')
        assert output[-1] == "host = localhost"

    def test_toMediaConvert3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toMediaConvert3Config())')
        assert output[-1] == "host = localhost\nport = 443"
