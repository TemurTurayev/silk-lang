"""
Tests for dict .toMemgraphConfig() method - Memgraph config format.
"""

from silk.interpreter import Interpreter


class TestDictToMemgraphConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMemgraphConfig_basic(self):
        output = self._run('print({"port": 7687}.toMemgraphConfig())')
        assert output[-1] == "port = 7687"

    def test_toMemgraphConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 7687}.toMemgraphConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 7687" in output[-1]
