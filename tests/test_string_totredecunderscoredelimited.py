"""
Tests for string .toTredecUnderscoreDelimited() method - join words with 13 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToTredecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toTredecUnderscoreDelimited())')
        assert output[-1] == "hello_____________world"

    def test_toTredecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toTredecUnderscoreDelimited())')
        assert output[-1] == "a_____________b_____________c"
