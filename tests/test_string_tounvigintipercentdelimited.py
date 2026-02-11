"""
Tests for string .toUnvigintiPercentDelimited() method - join words with 21 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiPercentDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiPercentDelimited())')
        assert output[-1] == "hello" + "%" * 21 + "world"

    def test_toUnvigintiPercentDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiPercentDelimited())')
        assert output[-1] == "a" + "%" * 21 + "b" + "%" * 21 + "c"
