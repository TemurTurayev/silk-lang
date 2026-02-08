"""
Tests for string .toQuadUnderscoreDelimited() method - split words by ____.
"""

from silk.interpreter import Interpreter


class TestStringToQuadUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toQuadUnderscoreDelimited())')
        assert output[-1] == "hello____world"

    def test_toQuadUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toQuadUnderscoreDelimited())')
        assert output[-1] == "a____b____c"
