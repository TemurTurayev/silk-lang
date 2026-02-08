"""
Tests for string .toSeptPercentDelimited() method - split words by %%%%%%%.
"""

from silk.interpreter import Interpreter


class TestStringToSeptPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptPercentDelimited_basic(self):
        output = self._run('print("hello world".toSeptPercentDelimited())')
        assert output[-1] == "hello%%%%%%%world"

    def test_toSeptPercentDelimited_three(self):
        output = self._run('print("a b c".toSeptPercentDelimited())')
        assert output[-1] == "a%%%%%%%b%%%%%%%c"
