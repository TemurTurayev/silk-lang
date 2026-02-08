"""
Tests for string .toDecEqualDelimited() method - split words by ========== (10 equals).
"""

from silk.interpreter import Interpreter


class TestStringToDecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecEqualDelimited_basic(self):
        output = self._run('print("hello world".toDecEqualDelimited())')
        assert output[-1] == "hello==========world"

    def test_toDecEqualDelimited_three(self):
        output = self._run('print("a b c".toDecEqualDelimited())')
        assert output[-1] == "a==========b==========c"
