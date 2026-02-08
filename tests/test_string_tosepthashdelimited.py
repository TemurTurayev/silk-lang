"""
Tests for string .toSeptHashDelimited() method - split words by #######.
"""

from silk.interpreter import Interpreter


class TestStringToSeptHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptHashDelimited_basic(self):
        output = self._run('print("hello world".toSeptHashDelimited())')
        assert output[-1] == "hello#######world"

    def test_toSeptHashDelimited_three(self):
        output = self._run('print("a b c".toSeptHashDelimited())')
        assert output[-1] == "a#######b#######c"
