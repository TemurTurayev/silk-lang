"""
Tests for dict .toMediaConnectConfig() method - format as AWS MediaConnect config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaConnectConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaConnectConfig_basic(self):
        output = self._run('print({"flow": "live"}.toMediaConnectConfig())')
        assert output[-1] == "flow = live"

    def test_toMediaConnectConfig_multi(self):
        output = self._run('print({"flow": "live", "protocol": "zixi"}.toMediaConnectConfig())')
        assert "flow = live" in output[-1]
