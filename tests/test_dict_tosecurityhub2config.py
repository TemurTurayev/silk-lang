"""
Tests for dict .toSecurityHub2Config() method - format as SecurityHub v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSecurityHub2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSecurityHub2Config_basic(self):
        output = self._run('print({"standard": "cis"}.toSecurityHub2Config())')
        assert output[-1] == "standard = cis"

    def test_toSecurityHub2Config_multi(self):
        output = self._run('print({"standard": "cis", "status": "active"}.toSecurityHub2Config())')
        assert output[-1] == "standard = cis\nstatus = active"
