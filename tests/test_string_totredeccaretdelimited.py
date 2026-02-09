"""
Tests for string .toTredecCaretDelimited() method - join words with 13 carets.
"""

from silk.interpreter import Interpreter


class TestStringToTredecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecCaretDelimited_basic(self):
        output = self._run('print("hello world".toTredecCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^^^^^world"

    def test_toTredecCaretDelimited_three(self):
        output = self._run('print("a b c".toTredecCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^^^^^b^^^^^^^^^^^^^c"
