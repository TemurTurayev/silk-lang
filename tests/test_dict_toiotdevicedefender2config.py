"""
Tests for dict .toIoTDeviceDefender2Config() method - format as IoT Device Defender config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTDeviceDefender2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTDeviceDefender2Config_basic(self):
        output = self._run('print({"profileName": "sec-profile"}.toIoTDeviceDefender2Config())')
        assert output[-1] == "profileName = sec-profile"

    def test_toIoTDeviceDefender2Config_multi(self):
        output = self._run('print({"profileName": "sec-profile", "targetArn": "arn:123"}.toIoTDeviceDefender2Config())')
        assert "profileName = sec-profile" in output[-1]
