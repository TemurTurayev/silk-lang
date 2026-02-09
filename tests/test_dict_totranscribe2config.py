"""
Tests for dict .toTranscribe2Config() method - format as Transcribe v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTranscribe2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTranscribe2Config_basic(self):
        output = self._run('print({"language": "en-US"}.toTranscribe2Config())')
        assert output[-1] == "language = en-US"

    def test_toTranscribe2Config_multi(self):
        output = self._run('print({"language": "en-US", "model": "medical"}.toTranscribe2Config())')
        assert output[-1] == "language = en-US\nmodel = medical"
