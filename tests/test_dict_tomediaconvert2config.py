"""
Tests for dict .toMediaConvert2Config() method - format as MediaConvert v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMediaConvert2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaConvert2Config_basic(self):
        output = self._run('print({"queue": "default"}.toMediaConvert2Config())')
        assert output[-1] == "queue = default"

    def test_toMediaConvert2Config_multi(self):
        output = self._run('print({"queue": "default", "codec": "h264"}.toMediaConvert2Config())')
        assert output[-1] == "queue = default\ncodec = h264"
