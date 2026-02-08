"""
Tests for string .toSextCaretDelimited() method - split words by ^^^^^^.
"""

from silk.interpreter import Interpreter


class TestStringToSextCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextCaretDelimited_basic(self):
        output = self._run('print("hello world".toSextCaretDelimited())')
        assert output[-1] == "hello^^^^^^world"

    def test_toSextCaretDelimited_three(self):
        output = self._run('print("a b c".toSextCaretDelimited())')
        assert output[-1] == "a^^^^^^b^^^^^^c"
