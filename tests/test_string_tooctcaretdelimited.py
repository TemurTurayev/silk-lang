"""
Tests for string .toOctCaretDelimited() method - split words by ^^^^^^^^.
"""

from silk.interpreter import Interpreter


class TestStringToOctCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctCaretDelimited_basic(self):
        output = self._run('print("hello world".toOctCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^world"

    def test_toOctCaretDelimited_three(self):
        output = self._run('print("a b c".toOctCaretDelimited())')
        assert output[-1] == "a^^^^^^^^b^^^^^^^^c"
