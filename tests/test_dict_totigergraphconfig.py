"""
Tests for dict .toTigerGraphConfig() method - TigerGraph config format.
"""

from silk.interpreter import Interpreter


class TestDictToTigerGraphConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTigerGraphConfig_basic(self):
        output = self._run('print({"port": 9000}.toTigerGraphConfig())')
        assert output[-1] == "port = 9000"

    def test_toTigerGraphConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 9000}.toTigerGraphConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 9000" in output[-1]
