"""
Tests for string .toEqualDelimited() method - split words by equals sign.
"""

from silk.interpreter import Interpreter


class TestStringToEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEqualDelimited_basic(self):
        output = self._run('print("hello world".toEqualDelimited())')
        assert output[-1] == "hello=world"

    def test_toEqualDelimited_three(self):
        output = self._run('print("a b c".toEqualDelimited())')
        assert output[-1] == "a=b=c"
