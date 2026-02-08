"""
Tests for dict .toCloudFormationConfig() method - format as CloudFormation config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudFormationConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudFormationConfig_basic(self):
        output = self._run('print({"stack": "prod-api"}.toCloudFormationConfig())')
        assert output[-1] == "stack = prod-api"

    def test_toCloudFormationConfig_multi(self):
        output = self._run('print({"template": "vpc.yaml", "region": "us-east-1"}.toCloudFormationConfig())')
        assert "template = vpc.yaml" in output[-1]
