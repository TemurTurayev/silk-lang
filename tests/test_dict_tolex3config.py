"""
Tests for dict .toLex3Config() method - format as Lex v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToLex3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLex3Config_basic(self):
        output = self._run('print({"bot": "order-bot"}.toLex3Config())')
        assert output[-1] == "bot = order-bot"

    def test_toLex3Config_multi(self):
        output = self._run('print({"bot": "order-bot", "locale": "en_US"}.toLex3Config())')
        assert output[-1] == "bot = order-bot\nlocale = en_US"
