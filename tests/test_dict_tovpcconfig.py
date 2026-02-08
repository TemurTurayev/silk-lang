"""
Tests for dict .toVPCConfig() method - format as AWS VPC config.
"""

from silk.interpreter import Interpreter


class TestDictToVPCConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVPCConfig_basic(self):
        output = self._run('print({"cidr": "10.0.0.0/16"}.toVPCConfig())')
        assert output[-1] == "cidr = 10.0.0.0/16"

    def test_toVPCConfig_multi(self):
        output = self._run('print({"cidr": "10.0.0.0/16", "tenancy": "default"}.toVPCConfig())')
        assert "cidr = 10.0.0.0/16" in output[-1]
