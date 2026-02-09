"""
Tests for string .toQuindecPercentDelimited() method - join words with 15 percent signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecPercentDelimited_basic(self):
        output = self._run('print("hello world".toQuindecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%%%%%%world"

    def test_toQuindecPercentDelimited_three(self):
        output = self._run('print("a b c".toQuindecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%%%%%%b%%%%%%%%%%%%%%%c"
