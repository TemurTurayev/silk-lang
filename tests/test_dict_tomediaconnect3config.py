"""
Tests for dict .toMediaConnect3Config() method - format dict as MediaConnect3 config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaConnect3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaConnect3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toMediaConnect3Config())')
        assert output[-1] == "host = localhost"

    def test_toMediaConnect3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toMediaConnect3Config())')
        assert output[-1] == "host = localhost\nport = 443"
