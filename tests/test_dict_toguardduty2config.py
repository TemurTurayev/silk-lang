"""
Tests for dict .toGuardDuty2Config() method - format as GuardDuty v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToGuardDuty2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGuardDuty2Config_basic(self):
        output = self._run('print({"detector": "main"}.toGuardDuty2Config())')
        assert output[-1] == "detector = main"

    def test_toGuardDuty2Config_multi(self):
        output = self._run('print({"detector": "main", "severity": "HIGH"}.toGuardDuty2Config())')
        assert output[-1] == "detector = main\nseverity = HIGH"
