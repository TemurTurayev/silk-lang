"""
Tests for dict .toMediaTailor3Config() method - format dict as MediaTailor3 config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaTailor3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaTailor3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toMediaTailor3Config())')
        assert output[-1] == "host = localhost"

    def test_toMediaTailor3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toMediaTailor3Config())')
        assert output[-1] == "host = localhost\nport = 443"
