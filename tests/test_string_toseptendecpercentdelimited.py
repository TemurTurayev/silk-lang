"""
Tests for string .toSeptendecPercentDelimited() method - join words with 17 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecPercentDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecPercentDelimited())')
        assert output[-1] == "hello" + "%" * 17 + "world"

    def test_toSeptendecPercentDelimited_three(self):
        output = self._run('print("a b c".toSeptendecPercentDelimited())')
        assert output[-1] == "a" + "%" * 17 + "b" + "%" * 17 + "c"
