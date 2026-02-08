"""
Tests for string .toQuintStarDelimited() method - split words by *****.
"""

from silk.interpreter import Interpreter


class TestStringToQuintStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintStarDelimited_basic(self):
        output = self._run('print("hello world".toQuintStarDelimited())')
        assert output[-1] == "hello*****world"

    def test_toQuintStarDelimited_three(self):
        output = self._run('print("a b c".toQuintStarDelimited())')
        assert output[-1] == "a*****b*****c"
