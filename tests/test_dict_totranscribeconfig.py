"""
Tests for dict .toTranscribeConfig() method - format as Transcribe config.
"""

from silk.interpreter import Interpreter


class TestDictToTranscribeConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTranscribeConfig_basic(self):
        output = self._run('print({"language": "en-US"}.toTranscribeConfig())')
        assert output[-1] == "language = en-US"

    def test_toTranscribeConfig_multi(self):
        output = self._run('print({"format": "wav", "channel": 1}.toTranscribeConfig())')
        assert "format = wav" in output[-1]
