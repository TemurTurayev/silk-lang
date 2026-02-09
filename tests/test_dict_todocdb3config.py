"""
Tests for dict .toDocDB3Config() method - format as DocumentDB v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToDocDB3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDocDB3Config_basic(self):
        output = self._run('print({"cluster": "docs"}.toDocDB3Config())')
        assert output[-1] == "cluster = docs"

    def test_toDocDB3Config_multi(self):
        output = self._run('print({"cluster": "docs", "instances": 3}.toDocDB3Config())')
        assert output[-1] == "cluster = docs\ninstances = 3"
