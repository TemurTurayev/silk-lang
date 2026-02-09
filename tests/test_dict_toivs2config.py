"""
Tests for dict .toIVS2Config() method - format as IVS v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToIVS2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIVS2Config_basic(self):
        output = self._run('print({"channel": "live"}.toIVS2Config())')
        assert output[-1] == "channel = live"

    def test_toIVS2Config_multi(self):
        output = self._run('print({"channel": "live", "latency": "low"}.toIVS2Config())')
        assert output[-1] == "channel = live\nlatency = low"
