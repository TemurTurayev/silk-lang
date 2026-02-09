"""
Tests for dict .toTranslate2Config() method - format as Translate v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTranslate2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTranslate2Config_basic(self):
        output = self._run('print({"source": "en"}.toTranslate2Config())')
        assert output[-1] == "source = en"

    def test_toTranslate2Config_multi(self):
        output = self._run('print({"source": "en", "target": "es"}.toTranslate2Config())')
        assert output[-1] == "source = en\ntarget = es"
