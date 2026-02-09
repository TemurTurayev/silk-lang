"""
Tests for dict .toIoTDeviceAdvisor2Config() method - format as IoT Device Advisor config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTDeviceAdvisor2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTDeviceAdvisor2Config_basic(self):
        output = self._run('print({"suiteName": "cert-suite"}.toIoTDeviceAdvisor2Config())')
        assert output[-1] == "suiteName = cert-suite"

    def test_toIoTDeviceAdvisor2Config_multi(self):
        output = self._run('print({"suiteName": "cert-suite", "deviceArn": "arn:456"}.toIoTDeviceAdvisor2Config())')
        assert "suiteName = cert-suite" in output[-1]
