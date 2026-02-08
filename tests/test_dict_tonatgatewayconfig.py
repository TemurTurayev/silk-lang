"""
Tests for dict .toNATGatewayConfig() method - format as AWS NAT Gateway config.
"""

from silk.interpreter import Interpreter


class TestDictToNATGatewayConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNATGatewayConfig_basic(self):
        output = self._run('print({"subnet": "subnet-abc"}.toNATGatewayConfig())')
        assert output[-1] == "subnet = subnet-abc"

    def test_toNATGatewayConfig_multi(self):
        output = self._run('print({"subnet": "subnet-abc", "eip": "eip-123"}.toNATGatewayConfig())')
        assert "subnet = subnet-abc" in output[-1]
