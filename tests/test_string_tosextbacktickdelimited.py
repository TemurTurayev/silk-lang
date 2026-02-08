"""
Tests for string .toSextBacktickDelimited() method - split words by ``````.
"""

from silk.interpreter import Interpreter


class TestStringToSextBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextBacktickDelimited_basic(self):
        output = self._run('print("hello world".toSextBacktickDelimited())')
        assert output[-1] == "hello``````world"

    def test_toSextBacktickDelimited_three(self):
        output = self._run('print("a b c".toSextBacktickDelimited())')
        assert output[-1] == "a``````b``````c"
