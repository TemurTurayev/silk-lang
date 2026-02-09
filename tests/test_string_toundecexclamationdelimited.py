"""
Tests for string .toUndecExclamationDelimited() method - split words by !!!!!!!!!!! (11 exclamation marks).
"""

from silk.interpreter import Interpreter


class TestStringToUndecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toUndecExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!!!world"

    def test_toUndecExclamationDelimited_three(self):
        output = self._run('print("a b c".toUndecExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!!!b!!!!!!!!!!!c"
