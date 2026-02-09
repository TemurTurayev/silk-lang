"""
Tests for dict .toKendra2Config() method - format as Kendra v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToKendra2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKendra2Config_basic(self):
        output = self._run('print({"index": "myIndex"}.toKendra2Config())')
        assert output[-1] == "index = myIndex"

    def test_toKendra2Config_multi(self):
        output = self._run('print({"index": "docs", "region": "us-west-2"}.toKendra2Config())')
        assert output[-1] == "index = docs\nregion = us-west-2"
