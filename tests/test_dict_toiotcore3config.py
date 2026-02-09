"""
Tests for dict .toIoTCore3Config() method - format as IoT Core v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIoTCore3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTCore3Config_basic(self):
        output = self._run('print({"endpoint": "iot.aws"}.toIoTCore3Config())')
        assert output[-1] == "endpoint = iot.aws"

    def test_toIoTCore3Config_multi(self):
        output = self._run('print({"endpoint": "iot.aws", "protocol": "mqtt"}.toIoTCore3Config())')
        assert output[-1] == "endpoint = iot.aws\nprotocol = mqtt"
