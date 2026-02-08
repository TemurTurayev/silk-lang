"""
Tests for string .toOctPercentDelimited() method - split words by %%%%%%%%%%.
"""

from silk.interpreter import Interpreter


class TestStringToOctPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctPercentDelimited_basic(self):
        output = self._run('print("hello world".toOctPercentDelimited())')
        assert output[-1] == "hello%%%%%%%%world"

    def test_toOctPercentDelimited_three(self):
        output = self._run('print("a b c".toOctPercentDelimited())')
        assert output[-1] == "a%%%%%%%%b%%%%%%%%c"
