"""
Tests for string .toQuadDotDelimited() method - split words by ....
"""

from silk.interpreter import Interpreter


class TestStringToQuadDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadDotDelimited_basic(self):
        output = self._run('print("hello world".toQuadDotDelimited())')
        assert output[-1] == "hello....world"

    def test_toQuadDotDelimited_three(self):
        output = self._run('print("a b c".toQuadDotDelimited())')
        assert output[-1] == "a....b....c"
