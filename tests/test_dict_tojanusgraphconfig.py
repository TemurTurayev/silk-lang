"""
Tests for dict .toJanusGraphConfig() method - JanusGraph config format.
"""

from silk.interpreter import Interpreter


class TestDictToJanusGraphConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toJanusGraphConfig_basic(self):
        output = self._run('print({"port": 8182}.toJanusGraphConfig())')
        assert output[-1] == "port = 8182"

    def test_toJanusGraphConfig_multi(self):
        output = self._run('print({"host": "localhost", "port": 8182}.toJanusGraphConfig())')
        assert "host = localhost" in output[-1]
        assert "port = 8182" in output[-1]
