"""
Tests for string .toNovemdecCaretDelimited() method - join words with 19 carets.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecCaretDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecCaretDelimited())')
        assert output[-1] == "hello" + "^" * 19 + "world"

    def test_toNovemdecCaretDelimited_three(self):
        output = self._run('print("a b c".toNovemdecCaretDelimited())')
        assert output[-1] == "a" + "^" * 19 + "b" + "^" * 19 + "c"
