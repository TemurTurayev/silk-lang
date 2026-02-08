"""
Tests for string .toNonPipeDelimited() method - split words by ||||||||| (9 pipes).
"""

from silk.interpreter import Interpreter


class TestStringToNonPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonPipeDelimited_basic(self):
        output = self._run('print("hello world".toNonPipeDelimited())')
        assert output[-1] == "hello|||||||||world"

    def test_toNonPipeDelimited_three(self):
        output = self._run('print("a b c".toNonPipeDelimited())')
        assert output[-1] == "a|||||||||b|||||||||c"
