"""
Tests for dict .toSubnetConfig() method - format as AWS Subnet config.
"""

from silk.interpreter import Interpreter


class TestDictToSubnetConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSubnetConfig_basic(self):
        output = self._run('print({"cidr": "10.0.1.0/24"}.toSubnetConfig())')
        assert output[-1] == "cidr = 10.0.1.0/24"

    def test_toSubnetConfig_multi(self):
        output = self._run('print({"cidr": "10.0.1.0/24", "az": "us-east-1a"}.toSubnetConfig())')
        assert "cidr = 10.0.1.0/24" in output[-1]
