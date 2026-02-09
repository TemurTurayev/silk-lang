"""
Tests for dict .toSecurityGroup2Config() method - format as SecurityGroup v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSecurityGroup2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSecurityGroup2Config_basic(self):
        output = self._run('print({"sg_id": "sg-abc"}.toSecurityGroup2Config())')
        assert output[-1] == "sg_id = sg-abc"

    def test_toSecurityGroup2Config_multi(self):
        output = self._run('print({"sg_id": "sg-abc", "protocol": "tcp"}.toSecurityGroup2Config())')
        assert output[-1] == "sg_id = sg-abc\nprotocol = tcp"
