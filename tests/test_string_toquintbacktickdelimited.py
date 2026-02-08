"""
Tests for string .toQuintBacktickDelimited() method - split words by `````.
"""

from silk.interpreter import Interpreter


class TestStringToQuintBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintBacktickDelimited_basic(self):
        output = self._run('print("hello world".toQuintBacktickDelimited())')
        assert output[-1] == "hello`````world"

    def test_toQuintBacktickDelimited_three(self):
        output = self._run('print("a b c".toQuintBacktickDelimited())')
        assert output[-1] == "a`````b`````c"
