"""
Tests for dict .toAlertManagerConfig() method - AlertManager config format.
"""

from silk.interpreter import Interpreter


class TestDictToAlertManagerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAlertManagerConfig_basic(self):
        output = self._run('print({"severity": "critical"}.toAlertManagerConfig())')
        assert output[-1] == "severity = critical"

    def test_toAlertManagerConfig_multi(self):
        output = self._run('print({"severity": "critical", "team": "ops"}.toAlertManagerConfig())')
        assert "severity = critical" in output[-1]
        assert "team = ops" in output[-1]
