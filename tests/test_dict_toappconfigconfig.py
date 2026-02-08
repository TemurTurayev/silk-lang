"""
Tests for dict .toAppConfigConfig() method - format as AppConfig config.
"""

from silk.interpreter import Interpreter


class TestDictToAppConfigConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppConfigConfig_basic(self):
        output = self._run('print({"env": "prod"}.toAppConfigConfig())')
        assert output[-1] == "env = prod"

    def test_toAppConfigConfig_multi(self):
        output = self._run('print({"feature": "dark_mode", "enabled": true}.toAppConfigConfig())')
        assert "enabled = true" in output[-1]
