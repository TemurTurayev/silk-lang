"""
Tests for string .toUndecEqualDelimited() method - split words by =========== (11 equals).
"""

from silk.interpreter import Interpreter


class TestStringToUndecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecEqualDelimited_basic(self):
        output = self._run('print("hello world".toUndecEqualDelimited())')
        assert output[-1] == "hello===========world"

    def test_toUndecEqualDelimited_three(self):
        output = self._run('print("a b c".toUndecEqualDelimited())')
        assert output[-1] == "a===========b===========c"
