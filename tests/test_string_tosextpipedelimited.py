"""
Tests for string .toSextPipeDelimited() method - split words by ||||||.
"""

from silk.interpreter import Interpreter


class TestStringToSextPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextPipeDelimited_basic(self):
        output = self._run('print("hello world".toSextPipeDelimited())')
        assert output[-1] == "hello||||||world"

    def test_toSextPipeDelimited_three(self):
        output = self._run('print("a b c".toSextPipeDelimited())')
        assert output[-1] == "a||||||b||||||c"
