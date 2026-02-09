"""
Tests for dict .toAPIGateway3Config() method - format as API Gateway v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAPIGateway3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAPIGateway3Config_basic(self):
        output = self._run('print({"stage": "prod"}.toAPIGateway3Config())')
        assert output[-1] == "stage = prod"

    def test_toAPIGateway3Config_multi(self):
        output = self._run('print({"stage": "prod", "region": "us-east-1"}.toAPIGateway3Config())')
        assert output[-1] == "stage = prod\nregion = us-east-1"
