"""
Tests for string .toSeptendecDotDelimited() method - join words with 17 dots.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecDotDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecDotDelimited())')
        assert output[-1] == "hello" + "." * 17 + "world"

    def test_toSeptendecDotDelimited_three(self):
        output = self._run('print("a b c".toSeptendecDotDelimited())')
        assert output[-1] == "a" + "." * 17 + "b" + "." * 17 + "c"
