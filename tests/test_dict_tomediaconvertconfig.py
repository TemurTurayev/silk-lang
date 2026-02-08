"""
Tests for dict .toMediaConvertConfig() method - format as AWS MediaConvert config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaConvertConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaConvertConfig_basic(self):
        output = self._run('print({"codec": "h264"}.toMediaConvertConfig())')
        assert output[-1] == "codec = h264"

    def test_toMediaConvertConfig_multi(self):
        output = self._run('print({"codec": "h264", "quality": "high"}.toMediaConvertConfig())')
        assert "codec = h264" in output[-1]
