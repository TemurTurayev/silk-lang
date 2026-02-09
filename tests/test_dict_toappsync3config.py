"""
Tests for dict .toAppSync3Config() method - format as AppSync v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAppSync3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppSync3Config_basic(self):
        output = self._run('print({"api": "graphql"}.toAppSync3Config())')
        assert output[-1] == "api = graphql"

    def test_toAppSync3Config_multi(self):
        output = self._run('print({"api": "graphql", "region": "us-east-1"}.toAppSync3Config())')
        assert output[-1] == "api = graphql\nregion = us-east-1"
