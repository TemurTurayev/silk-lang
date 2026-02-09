"""
Tests for dict .toChime2Config() method - format as Chime v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToChime2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toChime2Config_basic(self):
        output = self._run('print({"account": "main"}.toChime2Config())')
        assert output[-1] == "account = main"

    def test_toChime2Config_multi(self):
        output = self._run('print({"account": "main", "region": "us-east"}.toChime2Config())')
        assert output[-1] == "account = main\nregion = us-east"
