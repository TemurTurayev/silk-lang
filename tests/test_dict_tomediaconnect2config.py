"""
Tests for dict .toMediaConnect2Config() method - format as MediaConnect v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMediaConnect2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaConnect2Config_basic(self):
        output = self._run('print({"flow": "live"}.toMediaConnect2Config())')
        assert output[-1] == "flow = live"

    def test_toMediaConnect2Config_multi(self):
        output = self._run('print({"flow": "live", "protocol": "srt"}.toMediaConnect2Config())')
        assert output[-1] == "flow = live\nprotocol = srt"
