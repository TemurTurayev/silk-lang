"""
Tests for dict .toKendra3Config() method - format as Kendra v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToKendra3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKendra3Config_basic(self):
        output = self._run('print({"index": "docs-search"}.toKendra3Config())')
        assert output[-1] == "index = docs-search"

    def test_toKendra3Config_multi(self):
        output = self._run('print({"index": "docs-search", "edition": "enterprise"}.toKendra3Config())')
        assert output[-1] == "index = docs-search\nedition = enterprise"
