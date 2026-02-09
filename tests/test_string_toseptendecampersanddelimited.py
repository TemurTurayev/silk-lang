"""
Tests for string .toSeptendecAmpersandDelimited() method - join words with 17 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 17 + "world"

    def test_toSeptendecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toSeptendecAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 17 + "b" + "&" * 17 + "c"
