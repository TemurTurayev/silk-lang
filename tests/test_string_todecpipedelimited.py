"""
Tests for string .toDecPipeDelimited() method - split words by |||||||||| (10 pipes).
"""

from silk.interpreter import Interpreter


class TestStringToDecPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecPipeDelimited_basic(self):
        output = self._run('print("hello world".toDecPipeDelimited())')
        assert output[-1] == "hello||||||||||world"

    def test_toDecPipeDelimited_three(self):
        output = self._run('print("a b c".toDecPipeDelimited())')
        assert output[-1] == "a||||||||||b||||||||||c"
