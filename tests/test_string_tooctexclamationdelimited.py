"""
Tests for string .toOctExclamationDelimited() method - split words by !!!!!!!!.
"""

from silk.interpreter import Interpreter


class TestStringToOctExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctExclamationDelimited_basic(self):
        output = self._run('print("hello world".toOctExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!world"

    def test_toOctExclamationDelimited_three(self):
        output = self._run('print("a b c".toOctExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!b!!!!!!!!c"
