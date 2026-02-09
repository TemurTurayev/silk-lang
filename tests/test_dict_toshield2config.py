"""
Tests for dict .toShield2Config() method - format as Shield v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToShield2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toShield2Config_basic(self):
        output = self._run('print({"protection": "enabled"}.toShield2Config())')
        assert output[-1] == "protection = enabled"

    def test_toShield2Config_multi(self):
        output = self._run('print({"protection": "enabled", "tier": "advanced"}.toShield2Config())')
        assert output[-1] == "protection = enabled\ntier = advanced"
