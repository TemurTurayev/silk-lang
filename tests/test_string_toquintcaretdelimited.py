"""
Tests for string .toQuintCaretDelimited() method - split words by ^^^^^.
"""

from silk.interpreter import Interpreter


class TestStringToQuintCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintCaretDelimited_basic(self):
        output = self._run('print("hello world".toQuintCaretDelimited())')
        assert output[-1] == "hello^^^^^world"

    def test_toQuintCaretDelimited_three(self):
        output = self._run('print("a b c".toQuintCaretDelimited())')
        assert output[-1] == "a^^^^^b^^^^^c"
