"""
Tests for string .toSeptCaretDelimited() method - split words by ^^^^^^^.
"""

from silk.interpreter import Interpreter


class TestStringToSeptCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptCaretDelimited_basic(self):
        output = self._run('print("hello world".toSeptCaretDelimited())')
        assert output[-1] == "hello^^^^^^^world"

    def test_toSeptCaretDelimited_three(self):
        output = self._run('print("a b c".toSeptCaretDelimited())')
        assert output[-1] == "a^^^^^^^b^^^^^^^c"
