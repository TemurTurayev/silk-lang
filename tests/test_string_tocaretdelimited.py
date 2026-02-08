"""
Tests for string .toCaretDelimited() method - split words by caret.
"""

from silk.interpreter import Interpreter


class TestStringToCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCaretDelimited_basic(self):
        output = self._run('print("hello world".toCaretDelimited())')
        assert output[-1] == "hello^world"

    def test_toCaretDelimited_three(self):
        output = self._run('print("a b c".toCaretDelimited())')
        assert output[-1] == "a^b^c"
