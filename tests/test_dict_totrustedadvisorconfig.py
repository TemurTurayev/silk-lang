"""
Tests for dict .toTrustedAdvisorConfig() method - format as Trusted Advisor config.
"""

from silk.interpreter import Interpreter


class TestDictToTrustedAdvisorConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTrustedAdvisorConfig_basic(self):
        output = self._run('print({"category": "security"}.toTrustedAdvisorConfig())')
        assert output[-1] == "category = security"

    def test_toTrustedAdvisorConfig_multi(self):
        output = self._run('print({"check": "mfa", "status": "warning"}.toTrustedAdvisorConfig())')
        assert "check = mfa" in output[-1]
