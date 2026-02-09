"""
Tests for dict .toTrustedAdvisor2Config() method - format as Trusted Advisor v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTrustedAdvisor2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTrustedAdvisor2Config_basic(self):
        output = self._run('print({"category": "cost"}.toTrustedAdvisor2Config())')
        assert output[-1] == "category = cost"

    def test_toTrustedAdvisor2Config_multi(self):
        output = self._run('print({"category": "cost", "status": "warning"}.toTrustedAdvisor2Config())')
        assert output[-1] == "category = cost\nstatus = warning"
