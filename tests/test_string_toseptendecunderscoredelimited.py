"""
Tests for string .toSeptendecUnderscoreDelimited() method - join words with 17 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecUnderscoreDelimited())')
        assert output[-1] == "hello" + "_" * 17 + "world"

    def test_toSeptendecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toSeptendecUnderscoreDelimited())')
        assert output[-1] == "a" + "_" * 17 + "b" + "_" * 17 + "c"
