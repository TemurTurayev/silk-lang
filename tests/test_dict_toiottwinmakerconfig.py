"""
Tests for dict .toIoTTwinMakerConfig() method - format as IoT TwinMaker config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTTwinMakerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTTwinMakerConfig_basic(self):
        output = self._run('print({"workspace": "factory_1"}.toIoTTwinMakerConfig())')
        assert output[-1] == "workspace = factory_1"

    def test_toIoTTwinMakerConfig_multi(self):
        output = self._run('print({"entity": "pump", "component": "motor"}.toIoTTwinMakerConfig())')
        assert "component = motor" in output[-1]
