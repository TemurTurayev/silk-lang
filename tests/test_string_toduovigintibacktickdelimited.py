"""
Tests for string .toDuovigintiBacktickDelimited() method - join words with 22 backtick chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiBacktickDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiBacktickDelimited())')
        assert output[-1] == "hello" + "`" * 22 + "world"

    def test_toDuovigintiBacktickDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiBacktickDelimited())')
        assert output[-1] == "a" + "`" * 22 + "b" + "`" * 22 + "c"
