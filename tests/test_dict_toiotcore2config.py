"""
Tests for dict .toIoTCore2Config() method - format as IoT Core config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTCore2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTCore2Config_basic(self):
        output = self._run('print({"thingName": "sensor-1"}.toIoTCore2Config())')
        assert output[-1] == "thingName = sensor-1"

    def test_toIoTCore2Config_multi(self):
        output = self._run('print({"thingName": "sensor-1", "region": "us-west-2"}.toIoTCore2Config())')
        assert "thingName = sensor-1" in output[-1]
