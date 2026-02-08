"""
Tests for dict .toIoTAnalyticsConfig() method - format as IoT Analytics config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTAnalyticsConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTAnalyticsConfig_basic(self):
        output = self._run('print({"channel": "temp_data"}.toIoTAnalyticsConfig())')
        assert output[-1] == "channel = temp_data"

    def test_toIoTAnalyticsConfig_multi(self):
        output = self._run('print({"pipeline": "etl", "batch": 100}.toIoTAnalyticsConfig())')
        assert "batch = 100" in output[-1]
