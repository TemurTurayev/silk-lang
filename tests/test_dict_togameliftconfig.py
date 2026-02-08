"""
Tests for dict .toGameLiftConfig() method - format as Amazon GameLift config.
"""

from silk.interpreter import Interpreter


class TestDictToGameLiftConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGameLiftConfig_basic(self):
        output = self._run('print({"fleet": "main"}.toGameLiftConfig())')
        assert output[-1] == "fleet = main"

    def test_toGameLiftConfig_multi(self):
        output = self._run('print({"fleet": "main", "region": "us-east-1"}.toGameLiftConfig())')
        assert "fleet = main" in output[-1]
