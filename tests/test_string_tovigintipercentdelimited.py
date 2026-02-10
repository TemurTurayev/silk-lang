"""
Tests for string .toVigintiPercentDelimited() method - join words with 20 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiPercentDelimited_basic(self):
        output = self._run('print("hello world".toVigintiPercentDelimited())')
        assert output[-1] == "hello" + "%" * 20 + "world"

    def test_toVigintiPercentDelimited_multi(self):
        output = self._run('print("a b c".toVigintiPercentDelimited())')
        assert output[-1] == "a" + "%" * 20 + "b" + "%" * 20 + "c"
