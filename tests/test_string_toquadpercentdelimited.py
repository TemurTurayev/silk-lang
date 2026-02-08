"""
Tests for string .toQuadPercentDelimited() method - split words by %%%%.
"""

from silk.interpreter import Interpreter


class TestStringToQuadPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadPercentDelimited_basic(self):
        output = self._run('print("hello world".toQuadPercentDelimited())')
        assert output[-1] == "hello%%%%world"

    def test_toQuadPercentDelimited_three(self):
        output = self._run('print("a b c".toQuadPercentDelimited())')
        assert output[-1] == "a%%%%b%%%%c"
