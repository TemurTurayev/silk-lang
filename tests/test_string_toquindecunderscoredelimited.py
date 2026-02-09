"""
Tests for string .toQuindecUnderscoreDelimited() method - join words with 15 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toQuindecUnderscoreDelimited())')
        assert output[-1] == "hello_______________world"

    def test_toQuindecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toQuindecUnderscoreDelimited())')
        assert output[-1] == "a_______________b_______________c"
