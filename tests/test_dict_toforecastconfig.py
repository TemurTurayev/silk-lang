"""
Tests for dict .toForecastConfig() method - format as Forecast config.
"""

from silk.interpreter import Interpreter


class TestDictToForecastConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toForecastConfig_basic(self):
        output = self._run('print({"horizon": 30}.toForecastConfig())')
        assert output[-1] == "horizon = 30"

    def test_toForecastConfig_multi(self):
        output = self._run('print({"frequency": "daily", "algorithm": "arima"}.toForecastConfig())')
        assert "frequency = daily" in output[-1]
