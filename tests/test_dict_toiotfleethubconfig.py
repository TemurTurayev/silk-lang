"""
Tests for dict .toIoTFleetHubConfig() method - format as IoT Fleet Hub config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTFleetHubConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTFleetHubConfig_basic(self):
        output = self._run('print({"fleet": "sensors_v2"}.toIoTFleetHubConfig())')
        assert output[-1] == "fleet = sensors_v2"

    def test_toIoTFleetHubConfig_multi(self):
        output = self._run('print({"region": "us-east-1", "devices": 100}.toIoTFleetHubConfig())')
        assert "devices = 100" in output[-1]
