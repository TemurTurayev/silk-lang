"""
Tests for string .toQuattuordecUnderscoreDelimited() method - join words with 14 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecUnderscoreDelimited())')
        assert output[-1] == "hello______________world"

    def test_toQuattuordecUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecUnderscoreDelimited())')
        assert output[-1] == "a______________b______________c"
