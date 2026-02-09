"""
Tests for dict .toIoTFleetHub3Config() method - format as IoT Fleet Hub v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTFleetHub3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTFleetHub3Config_basic(self):
        output = self._run('print({"fleet": "production"}.toIoTFleetHub3Config())')
        assert output[-1] == "fleet = production"

    def test_toIoTFleetHub3Config_multi(self):
        output = self._run('print({"fleet": "production", "region": "us-east-1"}.toIoTFleetHub3Config())')
        assert output[-1] == "fleet = production\nregion = us-east-1"
