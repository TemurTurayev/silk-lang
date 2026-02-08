"""
Tests for string .toSeptPipeDelimited() method - split words by |||||||.
"""

from silk.interpreter import Interpreter


class TestStringToSeptPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptPipeDelimited_basic(self):
        output = self._run('print("hello world".toSeptPipeDelimited())')
        assert output[-1] == "hello|||||||world"

    def test_toSeptPipeDelimited_three(self):
        output = self._run('print("a b c".toSeptPipeDelimited())')
        assert output[-1] == "a|||||||b|||||||c"
