"""
Tests for dict .toLex2Config() method - format as Lex v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToLex2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLex2Config_basic(self):
        output = self._run('print({"bot": "myBot"}.toLex2Config())')
        assert output[-1] == "bot = myBot"

    def test_toLex2Config_multi(self):
        output = self._run('print({"bot": "orderBot", "locale": "en_US"}.toLex2Config())')
        assert output[-1] == "bot = orderBot\nlocale = en_US"
