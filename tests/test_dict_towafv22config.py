"""
Tests for dict .toWAFv22Config() method - format as WAFv2 v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToWAFv22Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWAFv22Config_basic(self):
        output = self._run('print({"scope": "REGIONAL"}.toWAFv22Config())')
        assert output[-1] == "scope = REGIONAL"

    def test_toWAFv22Config_multi(self):
        output = self._run('print({"scope": "REGIONAL", "rule": "block"}.toWAFv22Config())')
        assert output[-1] == "scope = REGIONAL\nrule = block"
