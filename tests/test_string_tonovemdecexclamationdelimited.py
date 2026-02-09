"""
Tests for string .toNovemdecExclamationDelimited() method - join words with 19 exclamation marks.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 19 + "world"

    def test_toNovemdecExclamationDelimited_three(self):
        output = self._run('print("a b c".toNovemdecExclamationDelimited())')
        assert output[-1] == "a" + "!" * 19 + "b" + "!" * 19 + "c"
