"""
Tests for dict .toRedshift3Config() method - format as Redshift v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToRedshift3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedshift3Config_basic(self):
        output = self._run('print({"cluster": "analytics"}.toRedshift3Config())')
        assert output[-1] == "cluster = analytics"

    def test_toRedshift3Config_multi(self):
        output = self._run('print({"cluster": "analytics", "nodeType": "dc2.large"}.toRedshift3Config())')
        assert output[-1] == "cluster = analytics\nnodeType = dc2.large"
