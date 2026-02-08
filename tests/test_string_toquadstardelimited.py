"""
Tests for string .toQuadStarDelimited() method - split words by ****.
"""

from silk.interpreter import Interpreter


class TestStringToQuadStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadStarDelimited_basic(self):
        output = self._run('print("hello world".toQuadStarDelimited())')
        assert output[-1] == "hello****world"

    def test_toQuadStarDelimited_three(self):
        output = self._run('print("a b c".toQuadStarDelimited())')
        assert output[-1] == "a****b****c"
