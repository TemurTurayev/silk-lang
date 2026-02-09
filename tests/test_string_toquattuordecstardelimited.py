"""
Tests for string .toQuattuordecStarDelimited() method - join words with 14 stars.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecStarDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecStarDelimited())')
        assert output[-1] == "hello**************world"

    def test_toQuattuordecStarDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecStarDelimited())')
        assert output[-1] == "a**************b**************c"
