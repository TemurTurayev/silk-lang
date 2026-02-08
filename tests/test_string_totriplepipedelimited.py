"""
Tests for string .toTriplePipeDelimited() method - split words by |||.
"""

from silk.interpreter import Interpreter


class TestStringToTriplePipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTriplePipeDelimited_basic(self):
        output = self._run('print("hello world".toTriplePipeDelimited())')
        assert output[-1] == "hello|||world"

    def test_toTriplePipeDelimited_three(self):
        output = self._run('print("a b c".toTriplePipeDelimited())')
        assert output[-1] == "a|||b|||c"
