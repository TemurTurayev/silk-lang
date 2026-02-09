"""
Tests for dict .toTranscribe3Config() method - format as Transcribe v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTranscribe3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTranscribe3Config_basic(self):
        output = self._run('print({"language": "en-US"}.toTranscribe3Config())')
        assert output[-1] == "language = en-US"

    def test_toTranscribe3Config_multi(self):
        output = self._run('print({"language": "en-US", "model": "medical"}.toTranscribe3Config())')
        assert output[-1] == "language = en-US\nmodel = medical"
