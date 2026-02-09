"""
Tests for dict .toCostExplorer2Config() method - format as Cost Explorer v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCostExplorer2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCostExplorer2Config_basic(self):
        output = self._run('print({"granularity": "DAILY"}.toCostExplorer2Config())')
        assert output[-1] == "granularity = DAILY"

    def test_toCostExplorer2Config_multi(self):
        output = self._run('print({"granularity": "DAILY", "metric": "BlendedCost"}.toCostExplorer2Config())')
        assert output[-1] == "granularity = DAILY\nmetric = BlendedCost"
