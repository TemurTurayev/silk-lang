"""
Tests for dict .toLexConfig() method - format as Lex config.
"""

from silk.interpreter import Interpreter


class TestDictToLexConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLexConfig_basic(self):
        output = self._run('print({"bot": "orderbot"}.toLexConfig())')
        assert output[-1] == "bot = orderbot"

    def test_toLexConfig_multi(self):
        output = self._run('print({"locale": "en_US", "version": 2}.toLexConfig())')
        assert "locale = en_US" in output[-1]
