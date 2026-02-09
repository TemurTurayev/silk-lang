"""
Tests for string .toTredecHashDelimited() method - join words with 13 hash signs.
"""

from silk.interpreter import Interpreter


class TestStringToTredecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecHashDelimited_basic(self):
        output = self._run('print("hello world".toTredecHashDelimited())')
        assert output[-1] == "hello#############world"

    def test_toTredecHashDelimited_three(self):
        output = self._run('print("a b c".toTredecHashDelimited())')
        assert output[-1] == "a#############b#############c"
