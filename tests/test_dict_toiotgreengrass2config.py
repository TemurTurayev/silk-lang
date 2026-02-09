"""
Tests for dict .toIoTGreengrass2Config() method - format as IoT Greengrass config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTGreengrass2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTGreengrass2Config_basic(self):
        output = self._run('print({"groupName": "factory-group"}.toIoTGreengrass2Config())')
        assert output[-1] == "groupName = factory-group"

    def test_toIoTGreengrass2Config_multi(self):
        output = self._run('print({"groupName": "factory-group", "coreDevice": "core-1"}.toIoTGreengrass2Config())')
        assert "groupName = factory-group" in output[-1]
