"""
Tests for dict .toMediaTailor2Config() method - format as MediaTailor v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMediaTailor2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaTailor2Config_basic(self):
        output = self._run('print({"source": "hls"}.toMediaTailor2Config())')
        assert output[-1] == "source = hls"

    def test_toMediaTailor2Config_multi(self):
        output = self._run('print({"source": "hls", "ad": "vast"}.toMediaTailor2Config())')
        assert output[-1] == "source = hls\nad = vast"
