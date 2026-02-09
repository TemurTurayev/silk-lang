"""
Tests for dict .toConnect3Config() method - format dict as Connect3 config.
"""

from silk.interpreter import Interpreter


class TestDictToConnect3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toConnect3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toConnect3Config())')
        assert output[-1] == "host = localhost"

    def test_toConnect3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toConnect3Config())')
        assert output[-1] == "host = localhost\nport = 443"
