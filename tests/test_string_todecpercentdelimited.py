"""
Tests for string .toDecPercentDelimited() method - split words by %%%%%%%%%% (10 percents).
"""

from silk.interpreter import Interpreter


class TestStringToDecPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecPercentDelimited_basic(self):
        output = self._run('print("hello world".toDecPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%%%world"

    def test_toDecPercentDelimited_three(self):
        output = self._run('print("a b c".toDecPercentDelimited())')
        assert output[-1] == "a%%%%%%%%%%b%%%%%%%%%%c"
