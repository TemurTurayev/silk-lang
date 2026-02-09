"""
Tests for dict .toSNS3Config() method - format as SNS v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSNS3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSNS3Config_basic(self):
        output = self._run('print({"topic": "alerts"}.toSNS3Config())')
        assert output[-1] == "topic = alerts"

    def test_toSNS3Config_multi(self):
        output = self._run('print({"topic": "alerts", "protocol": "https"}.toSNS3Config())')
        assert output[-1] == "topic = alerts\nprotocol = https"
