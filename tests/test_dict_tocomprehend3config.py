"""
Tests for dict .toComprehend3Config() method - format as Comprehend v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToComprehend3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toComprehend3Config_basic(self):
        output = self._run('print({"language": "en"}.toComprehend3Config())')
        assert output[-1] == "language = en"

    def test_toComprehend3Config_multi(self):
        output = self._run('print({"language": "en", "model": "custom"}.toComprehend3Config())')
        assert output[-1] == "language = en\nmodel = custom"
