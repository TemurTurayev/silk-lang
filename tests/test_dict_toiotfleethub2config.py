"""
Tests for dict .toIoTFleetHub2Config() method - format as IoT FleetHub config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTFleetHub2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTFleetHub2Config_basic(self):
        output = self._run('print({"appName": "fleet-app"}.toIoTFleetHub2Config())')
        assert output[-1] == "appName = fleet-app"

    def test_toIoTFleetHub2Config_multi(self):
        output = self._run('print({"appName": "fleet-app", "region": "eu-west-1"}.toIoTFleetHub2Config())')
        assert "appName = fleet-app" in output[-1]
