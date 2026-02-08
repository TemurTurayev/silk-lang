"""
Tests for dict .toNebulaGraphConfig() method - NebulaGraph config format.
"""

from silk.interpreter import Interpreter


class TestDictToNebulaGraphConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNebulaGraphConfig_basic(self):
        output = self._run('print({"port": 9669}.toNebulaGraphConfig())')
        assert output[-1] == "port = 9669"

    def test_toNebulaGraphConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 9669}.toNebulaGraphConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 9669" in output[-1]
