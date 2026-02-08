"""
Tests for dict .toMediaLiveConfig() method - format as AWS MediaLive config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaLiveConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaLiveConfig_basic(self):
        output = self._run('print({"channel": "live1"}.toMediaLiveConfig())')
        assert output[-1] == "channel = live1"

    def test_toMediaLiveConfig_multi(self):
        output = self._run('print({"channel": "live1", "codec": "avc"}.toMediaLiveConfig())')
        assert "channel = live1" in output[-1]
