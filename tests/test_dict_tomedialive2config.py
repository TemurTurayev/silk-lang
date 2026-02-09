"""
Tests for dict .toMediaLive2Config() method - format as MediaLive v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMediaLive2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaLive2Config_basic(self):
        output = self._run('print({"channel": "live"}.toMediaLive2Config())')
        assert output[-1] == "channel = live"

    def test_toMediaLive2Config_multi(self):
        output = self._run('print({"channel": "live", "resolution": "1080p"}.toMediaLive2Config())')
        assert output[-1] == "channel = live\nresolution = 1080p"
