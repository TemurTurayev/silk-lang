"""
Tests for string .toQuadPipeDelimited() method - split words by ||||.
"""

from silk.interpreter import Interpreter


class TestStringToQuadPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadPipeDelimited_basic(self):
        output = self._run('print("hello world".toQuadPipeDelimited())')
        assert output[-1] == "hello||||world"

    def test_toQuadPipeDelimited_three(self):
        output = self._run('print("a b c".toQuadPipeDelimited())')
        assert output[-1] == "a||||b||||c"
