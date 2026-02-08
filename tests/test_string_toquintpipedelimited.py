"""
Tests for string .toQuintPipeDelimited() method - split words by |||||.
"""

from silk.interpreter import Interpreter


class TestStringToQuintPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintPipeDelimited_basic(self):
        output = self._run('print("hello world".toQuintPipeDelimited())')
        assert output[-1] == "hello|||||world"

    def test_toQuintPipeDelimited_three(self):
        output = self._run('print("a b c".toQuintPipeDelimited())')
        assert output[-1] == "a|||||b|||||c"
