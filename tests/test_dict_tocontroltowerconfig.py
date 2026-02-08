"""
Tests for dict .toControlTowerConfig() method - format as Control Tower config.
"""

from silk.interpreter import Interpreter


class TestDictToControlTowerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toControlTowerConfig_basic(self):
        output = self._run('print({"landing_zone": "default"}.toControlTowerConfig())')
        assert output[-1] == "landing_zone = default"

    def test_toControlTowerConfig_multi(self):
        output = self._run('print({"guardrail": "mandatory", "region": "us-east-1"}.toControlTowerConfig())')
        assert "guardrail = mandatory" in output[-1]
