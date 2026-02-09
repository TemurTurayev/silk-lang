"""
Tests for string .toOctodecCaretDelimited() method - join words with 18 carets.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecCaretDelimited_basic(self):
        output = self._run('print("hello world".toOctodecCaretDelimited())')
        assert output[-1] == "hello" + "^" * 18 + "world"

    def test_toOctodecCaretDelimited_three(self):
        output = self._run('print("a b c".toOctodecCaretDelimited())')
        assert output[-1] == "a" + "^" * 18 + "b" + "^" * 18 + "c"
