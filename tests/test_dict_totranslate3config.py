"""
Tests for dict .toTranslate3Config() method - format as Translate v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTranslate3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTranslate3Config_basic(self):
        output = self._run('print({"source": "en"}.toTranslate3Config())')
        assert output[-1] == "source = en"

    def test_toTranslate3Config_multi(self):
        output = self._run('print({"source": "en", "target": "es"}.toTranslate3Config())')
        assert output[-1] == "source = en\ntarget = es"
