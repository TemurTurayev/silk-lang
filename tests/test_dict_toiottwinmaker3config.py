"""
Tests for dict .toIoTTwinMaker3Config() method - format as IoT TwinMaker v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTTwinMaker3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTTwinMaker3Config_basic(self):
        output = self._run('print({"workspace": "factory"}.toIoTTwinMaker3Config())')
        assert output[-1] == "workspace = factory"

    def test_toIoTTwinMaker3Config_multi(self):
        output = self._run('print({"workspace": "factory", "scene": "floor1"}.toIoTTwinMaker3Config())')
        assert output[-1] == "workspace = factory\nscene = floor1"
