"""
Tests for string .toQuintPercentDelimited() method - split words by %%%%%.
"""

from silk.interpreter import Interpreter


class TestStringToQuintPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintPercentDelimited_basic(self):
        output = self._run('print("hello world".toQuintPercentDelimited())')
        assert output[-1] == "hello%%%%%world"

    def test_toQuintPercentDelimited_three(self):
        output = self._run('print("a b c".toQuintPercentDelimited())')
        assert output[-1] == "a%%%%%b%%%%%c"
