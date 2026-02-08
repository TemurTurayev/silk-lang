"""
Tests for dict .toProtonConfig() method - format as Proton config.
"""

from silk.interpreter import Interpreter


class TestDictToProtonConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toProtonConfig_basic(self):
        output = self._run('print({"service": "api"}.toProtonConfig())')
        assert output[-1] == "service = api"

    def test_toProtonConfig_multi(self):
        output = self._run('print({"template": "fargate", "environment": "prod"}.toProtonConfig())')
        assert "template = fargate" in output[-1]
