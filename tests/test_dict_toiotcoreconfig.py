"""
Tests for dict .toIoTCoreConfig() method - format as IoT Core config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTCoreConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTCoreConfig_basic(self):
        output = self._run('print({"topic": "sensors"}.toIoTCoreConfig())')
        assert output[-1] == "topic = sensors"

    def test_toIoTCoreConfig_multi(self):
        output = self._run('print({"qos": 1, "retain": true}.toIoTCoreConfig())')
        assert "qos = 1" in output[-1]
