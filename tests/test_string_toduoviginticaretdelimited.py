"""
Tests for string .toDuovigintiCaretDelimited() method - join words with 22 caret chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiCaretDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiCaretDelimited())')
        assert output[-1] == "hello" + "^" * 22 + "world"

    def test_toDuovigintiCaretDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiCaretDelimited())')
        assert output[-1] == "a" + "^" * 22 + "b" + "^" * 22 + "c"
