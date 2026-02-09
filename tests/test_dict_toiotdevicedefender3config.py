"""
Tests for dict .toIoTDeviceDefender3Config() method - format as IoT Device Defender v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTDeviceDefender3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTDeviceDefender3Config_basic(self):
        output = self._run('print({"audit": "enabled"}.toIoTDeviceDefender3Config())')
        assert output[-1] == "audit = enabled"

    def test_toIoTDeviceDefender3Config_multi(self):
        output = self._run('print({"audit": "enabled", "interval": 300}.toIoTDeviceDefender3Config())')
        assert output[-1] == "audit = enabled\ninterval = 300"
