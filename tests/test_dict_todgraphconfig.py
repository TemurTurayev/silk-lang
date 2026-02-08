"""
Tests for dict .toDgraphConfig() method - Dgraph config format.
"""

from silk.interpreter import Interpreter


class TestDictToDgraphConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDgraphConfig_basic(self):
        output = self._run('print({"port": 8080}.toDgraphConfig())')
        assert output[-1] == "port = 8080"

    def test_toDgraphConfig_string(self):
        output = self._run('print({"host": "localhost"}.toDgraphConfig())')
        assert output[-1] == "host = localhost"
