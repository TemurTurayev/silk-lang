"""
Tests for dict .toGameLift2Config() method - format as GameLift v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToGameLift2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGameLift2Config_basic(self):
        output = self._run('print({"fleet": "spot"}.toGameLift2Config())')
        assert output[-1] == "fleet = spot"

    def test_toGameLift2Config_multi(self):
        output = self._run('print({"fleet": "spot", "region": "us-west"}.toGameLift2Config())')
        assert output[-1] == "fleet = spot\nregion = us-west"
