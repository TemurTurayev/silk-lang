"""
Tests for dict .toIoTDeviceDefenderConfig() method - format as IoT Device Defender config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTDeviceDefenderConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTDeviceDefenderConfig_basic(self):
        output = self._run('print({"audit": "enabled"}.toIoTDeviceDefenderConfig())')
        assert output[-1] == "audit = enabled"

    def test_toIoTDeviceDefenderConfig_multi(self):
        output = self._run('print({"check": "cert_expiry", "days": 30}.toIoTDeviceDefenderConfig())')
        assert "days = 30" in output[-1]
