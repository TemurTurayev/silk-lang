"""
Tests for dict .toTranslateConfig() method - format as Translate config.
"""

from silk.interpreter import Interpreter


class TestDictToTranslateConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTranslateConfig_basic(self):
        output = self._run('print({"source": "en"}.toTranslateConfig())')
        assert output[-1] == "source = en"

    def test_toTranslateConfig_multi(self):
        output = self._run('print({"target": "fr", "formality": "formal"}.toTranslateConfig())')
        assert "target = fr" in output[-1]
