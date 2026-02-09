"""
Tests for string .toDecUnderscoreDelimited() method - split words by __________ (10 underscores).
"""

from silk.interpreter import Interpreter


class TestStringToDecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toDecUnderscoreDelimited())')
        assert output[-1] == "hello__________world"

    def test_toDecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toDecUnderscoreDelimited())')
        assert output[-1] == "a__________b__________c"
