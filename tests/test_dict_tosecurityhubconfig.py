"""
Tests for dict .toSecurityHubConfig() method - format as Security Hub config.
"""

from silk.interpreter import Interpreter


class TestDictToSecurityHubConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSecurityHubConfig_basic(self):
        output = self._run('print({"standard": "cis"}.toSecurityHubConfig())')
        assert output[-1] == "standard = cis"

    def test_toSecurityHubConfig_multi(self):
        output = self._run('print({"auto_enable": "true", "region": "us-west-2"}.toSecurityHubConfig())')
        assert "auto_enable = true" in output[-1]
