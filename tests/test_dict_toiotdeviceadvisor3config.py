"""
Tests for dict .toIoTDeviceAdvisor3Config() method - format as IoT Device Advisor v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTDeviceAdvisor3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTDeviceAdvisor3Config_basic(self):
        output = self._run('print({"suite": "mqtt-test"}.toIoTDeviceAdvisor3Config())')
        assert output[-1] == "suite = mqtt-test"

    def test_toIoTDeviceAdvisor3Config_multi(self):
        output = self._run('print({"suite": "mqtt-test", "timeout": 60}.toIoTDeviceAdvisor3Config())')
        assert output[-1] == "suite = mqtt-test\ntimeout = 60"
