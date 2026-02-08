"""
Tests for dict .toIoTDeviceAdvisorConfig() method - format as IoT Device Advisor config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTDeviceAdvisorConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTDeviceAdvisorConfig_basic(self):
        output = self._run('print({"suite": "mqtt_connect"}.toIoTDeviceAdvisorConfig())')
        assert output[-1] == "suite = mqtt_connect"

    def test_toIoTDeviceAdvisorConfig_multi(self):
        output = self._run('print({"protocol": "mqtt", "timeout": 60}.toIoTDeviceAdvisorConfig())')
        assert "timeout = 60" in output[-1]
