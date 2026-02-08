"""
Tests for dict .toCosmosDBConfig() method - CosmosDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToCosmosDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCosmosDBConfig_basic(self):
        output = self._run('print({"port": 443}.toCosmosDBConfig())')
        assert output[-1] == "port = 443"

    def test_toCosmosDBConfig_string(self):
        output = self._run('print({"endpoint": "cosmos.db"}.toCosmosDBConfig())')
        assert output[-1] == "endpoint = cosmos.db"
