"""
Tests for dict .toForecast3Config() method - format as Forecast v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToForecast3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toForecast3Config_basic(self):
        output = self._run('print({"dataset": "retail-demand"}.toForecast3Config())')
        assert output[-1] == "dataset = retail-demand"

    def test_toForecast3Config_multi(self):
        output = self._run('print({"dataset": "retail-demand", "horizon": 30}.toForecast3Config())')
        assert output[-1] == "dataset = retail-demand\nhorizon = 30"
