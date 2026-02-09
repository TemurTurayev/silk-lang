"""
Tests for dict .toIoTGreengrass3Config() method - format as IoT Greengrass v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTGreengrass3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTGreengrass3Config_basic(self):
        output = self._run('print({"core": "edge-01"}.toIoTGreengrass3Config())')
        assert output[-1] == "core = edge-01"

    def test_toIoTGreengrass3Config_multi(self):
        output = self._run('print({"core": "edge-01", "group": "factory"}.toIoTGreengrass3Config())')
        assert output[-1] == "core = edge-01\ngroup = factory"
