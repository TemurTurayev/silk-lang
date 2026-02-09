"""
Tests for dict .toAPIGateway2Config() method - format as API Gateway config.
"""

from silk.interpreter import Interpreter


class TestDictToAPIGateway2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAPIGateway2Config_basic(self):
        output = self._run('print({"apiName": "my-api"}.toAPIGateway2Config())')
        assert output[-1] == "apiName = my-api"

    def test_toAPIGateway2Config_multi(self):
        output = self._run('print({"apiName": "my-api", "stage": "prod"}.toAPIGateway2Config())')
        assert "apiName = my-api" in output[-1]
