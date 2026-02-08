"""
Tests for dict .toPollyConfig() method - format as Polly config.
"""

from silk.interpreter import Interpreter


class TestDictToPollyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPollyConfig_basic(self):
        output = self._run('print({"voice": "joanna"}.toPollyConfig())')
        assert output[-1] == "voice = joanna"

    def test_toPollyConfig_multi(self):
        output = self._run('print({"engine": "neural", "language": "en"}.toPollyConfig())')
        assert "engine = neural" in output[-1]
