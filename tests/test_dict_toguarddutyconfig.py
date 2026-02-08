"""
Tests for dict .toGuardDutyConfig() method - format as GuardDuty config.
"""

from silk.interpreter import Interpreter


class TestDictToGuardDutyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGuardDutyConfig_basic(self):
        output = self._run('print({"detector": "main"}.toGuardDutyConfig())')
        assert output[-1] == "detector = main"

    def test_toGuardDutyConfig_multi(self):
        output = self._run('print({"frequency": "hourly", "enabled": true}.toGuardDutyConfig())')
        assert "frequency = hourly" in output[-1]
