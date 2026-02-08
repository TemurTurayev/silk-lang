"""
Tests for string .toQuadBacktickDelimited() method - split words by ````.
"""

from silk.interpreter import Interpreter


class TestStringToQuadBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadBacktickDelimited_basic(self):
        output = self._run('print("hello world".toQuadBacktickDelimited())')
        assert output[-1] == "hello````world"

    def test_toQuadBacktickDelimited_three(self):
        output = self._run('print("a b c".toQuadBacktickDelimited())')
        assert output[-1] == "a````b````c"
