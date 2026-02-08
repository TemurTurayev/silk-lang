"""
Tests for string .toOctPipeDelimited() method - split words by ||||||||.
"""

from silk.interpreter import Interpreter


class TestStringToOctPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctPipeDelimited_basic(self):
        output = self._run('print("hello world".toOctPipeDelimited())')
        assert output[-1] == "hello||||||||world"

    def test_toOctPipeDelimited_three(self):
        output = self._run('print("a b c".toOctPipeDelimited())')
        assert output[-1] == "a||||||||b||||||||c"
