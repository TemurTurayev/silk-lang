"""
Tests for dict .toTerraformConfig() method - Terraform config format.
"""

from silk.interpreter import Interpreter


class TestDictToTerraformConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTerraformConfig_basic(self):
        output = self._run('print({"region": "us-east-1"}.toTerraformConfig())')
        assert output[-1] == 'region = "us-east-1"'

    def test_toTerraformConfig_multi(self):
        output = self._run('print({"region": "us-east-1", "count": 3}.toTerraformConfig())')
        assert 'region = "us-east-1"' in output[-1]
        assert "count = 3" in output[-1]
