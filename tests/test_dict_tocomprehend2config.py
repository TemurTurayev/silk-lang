"""
Tests for dict .toComprehend2Config() method - format as Comprehend v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToComprehend2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toComprehend2Config_basic(self):
        output = self._run('print({"language": "en"}.toComprehend2Config())')
        assert output[-1] == "language = en"

    def test_toComprehend2Config_multi(self):
        output = self._run('print({"language": "en", "mode": "sentiment"}.toComprehend2Config())')
        assert output[-1] == "language = en\nmode = sentiment"
