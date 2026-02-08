"""
Tests for dict .toSecurityGroupConfig() method - format as AWS Security Group config.
"""

from silk.interpreter import Interpreter


class TestDictToSecurityGroupConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSecurityGroupConfig_basic(self):
        output = self._run('print({"name": "web-sg"}.toSecurityGroupConfig())')
        assert output[-1] == "name = web-sg"

    def test_toSecurityGroupConfig_multi(self):
        output = self._run('print({"name": "web-sg", "vpc": "vpc-123"}.toSecurityGroupConfig())')
        assert "name = web-sg" in output[-1]
