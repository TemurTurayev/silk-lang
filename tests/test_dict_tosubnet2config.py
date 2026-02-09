"""
Tests for dict .toSubnet2Config() method - format as Subnet v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSubnet2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSubnet2Config_basic(self):
        output = self._run('print({"subnet_id": "subnet-abc"}.toSubnet2Config())')
        assert output[-1] == "subnet_id = subnet-abc"

    def test_toSubnet2Config_multi(self):
        output = self._run('print({"subnet_id": "subnet-abc", "cidr": "10.0.1.0/24"}.toSubnet2Config())')
        assert output[-1] == "subnet_id = subnet-abc\ncidr = 10.0.1.0/24"
