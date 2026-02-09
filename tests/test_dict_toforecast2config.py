"""
Tests for dict .toForecast2Config() method - format as Forecast v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToForecast2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toForecast2Config_basic(self):
        output = self._run('print({"predictor": "myPredictor"}.toForecast2Config())')
        assert output[-1] == "predictor = myPredictor"

    def test_toForecast2Config_multi(self):
        output = self._run('print({"predictor": "sales", "horizon": 30}.toForecast2Config())')
        assert output[-1] == "predictor = sales\nhorizon = 30"
