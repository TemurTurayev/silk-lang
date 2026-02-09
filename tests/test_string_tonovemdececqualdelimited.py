"""
Tests for string .toNovemdecEqualDelimited() method - join words with 19 equals signs.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecEqualDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecEqualDelimited())')
        assert output[-1] == "hello" + "=" * 19 + "world"

    def test_toNovemdecEqualDelimited_three(self):
        output = self._run('print("a b c".toNovemdecEqualDelimited())')
        assert output[-1] == "a" + "=" * 19 + "b" + "=" * 19 + "c"
