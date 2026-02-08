"""
Tests for string .toNonCaretDelimited() method - split words by ^^^^^^^^^ (9 carets).
"""

from silk.interpreter import Interpreter


class TestStringToNonCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonCaretDelimited_basic(self):
        output = self._run('print("hello world".toNonCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^world"

    def test_toNonCaretDelimited_three(self):
        output = self._run('print("a b c".toNonCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^b^^^^^^^^^c"
