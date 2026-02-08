"""
Tests for dict .toAPIGatewayConfig() method - format as API Gateway config.
"""

from silk.interpreter import Interpreter


class TestDictToAPIGatewayConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAPIGatewayConfig_basic(self):
        output = self._run('print({"stage": "prod"}.toAPIGatewayConfig())')
        assert output[-1] == "stage = prod"

    def test_toAPIGatewayConfig_multi(self):
        output = self._run('print({"method": "GET", "path": "/users"}.toAPIGatewayConfig())')
        assert "path = /users" in output[-1]
