"""
Tests for dict .toTiDBConfig() method - TiDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToTiDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTiDBConfig_basic(self):
        output = self._run('print({"port": 4000}.toTiDBConfig())')
        assert output[-1] == "port = 4000"

    def test_toTiDBConfig_string(self):
        output = self._run('print({"host": "localhost"}.toTiDBConfig())')
        assert output[-1] == "host = localhost"
