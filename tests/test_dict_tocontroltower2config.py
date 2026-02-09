"""
Tests for dict .toControlTower2Config() method - format as ControlTower v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToControlTower2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toControlTower2Config_basic(self):
        output = self._run('print({"landing_zone": "v3"}.toControlTower2Config())')
        assert output[-1] == "landing_zone = v3"

    def test_toControlTower2Config_multi(self):
        output = self._run('print({"landing_zone": "v3", "guardrails": "enabled"}.toControlTower2Config())')
        assert output[-1] == "landing_zone = v3\nguardrails = enabled"
