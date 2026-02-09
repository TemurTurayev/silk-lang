"""
Tests for string .toOctodecExclamationDelimited() method - join words with 18 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toOctodecExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 18 + "world"

    def test_toOctodecExclamationDelimited_three(self):
        output = self._run('print("a b c".toOctodecExclamationDelimited())')
        assert output[-1] == "a" + "!" * 18 + "b" + "!" * 18 + "c"
