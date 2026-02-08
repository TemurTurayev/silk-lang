"""
Tests for string .toSeptBacktickDelimited() method - split words by ```````.
"""

from silk.interpreter import Interpreter


class TestStringToSeptBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptBacktickDelimited_basic(self):
        output = self._run('print("hello world".toSeptBacktickDelimited())')
        assert output[-1] == "hello```````world"

    def test_toSeptBacktickDelimited_three(self):
        output = self._run('print("a b c".toSeptBacktickDelimited())')
        assert output[-1] == "a```````b```````c"
