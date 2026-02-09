"""
Tests for string .toNovemdecAmpersandDelimited() method - join words with 19 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 19 + "world"

    def test_toNovemdecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toNovemdecAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 19 + "b" + "&" * 19 + "c"
