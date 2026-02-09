"""
Tests for dict .toIoTAnalytics3Config() method - format as IoT Analytics v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTAnalytics3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTAnalytics3Config_basic(self):
        output = self._run('print({"channel": "temp"}.toIoTAnalytics3Config())')
        assert output[-1] == "channel = temp"

    def test_toIoTAnalytics3Config_multi(self):
        output = self._run('print({"channel": "temp", "dataset": "raw"}.toIoTAnalytics3Config())')
        assert output[-1] == "channel = temp\ndataset = raw"
