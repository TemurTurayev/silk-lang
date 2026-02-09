"""
Tests for string .toTredecEqualDelimited() method - join words with 13 equal signs.
"""

from silk.interpreter import Interpreter


class TestStringToTredecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecEqualDelimited_basic(self):
        output = self._run('print("hello world".toTredecEqualDelimited())')
        assert output[-1] == "hello=============world"

    def test_toTredecEqualDelimited_three(self):
        output = self._run('print("a b c".toTredecEqualDelimited())')
        assert output[-1] == "a=============b=============c"
