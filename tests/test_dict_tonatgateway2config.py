"""
Tests for dict .toNATGateway2Config() method - format as NATGateway v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToNATGateway2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNATGateway2Config_basic(self):
        output = self._run('print({"nat_id": "nat-123"}.toNATGateway2Config())')
        assert output[-1] == "nat_id = nat-123"

    def test_toNATGateway2Config_multi(self):
        output = self._run('print({"nat_id": "nat-123", "type": "public"}.toNATGateway2Config())')
        assert output[-1] == "nat_id = nat-123\ntype = public"
