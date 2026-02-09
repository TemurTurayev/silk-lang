"""
Tests for dict .toVPC2Config() method - format as VPC v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToVPC2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVPC2Config_basic(self):
        output = self._run('print({"vpc_id": "vpc-123"}.toVPC2Config())')
        assert output[-1] == "vpc_id = vpc-123"

    def test_toVPC2Config_multi(self):
        output = self._run('print({"vpc_id": "vpc-123", "cidr": "10.0.0.0/16"}.toVPC2Config())')
        assert output[-1] == "vpc_id = vpc-123\ncidr = 10.0.0.0/16"
