"""
Tests for string .toQuadAmpersandDelimited() method - split words by &&&&.
"""

from silk.interpreter import Interpreter


class TestStringToQuadAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toQuadAmpersandDelimited())')
        assert output[-1] == "hello&&&&world"

    def test_toQuadAmpersandDelimited_three(self):
        output = self._run('print("a b c".toQuadAmpersandDelimited())')
        assert output[-1] == "a&&&&b&&&&c"
