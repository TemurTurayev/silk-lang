"""
Tests for string .toUndecCaretDelimited() method - split words by ^^^^^^^^^^^ (11 carets).
"""

from silk.interpreter import Interpreter


class TestStringToUndecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecCaretDelimited_basic(self):
        output = self._run('print("hello world".toUndecCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^^^world"

    def test_toUndecCaretDelimited_three(self):
        output = self._run('print("a b c".toUndecCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^^^b^^^^^^^^^^^c"
