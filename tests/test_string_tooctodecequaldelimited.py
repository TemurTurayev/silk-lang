"""
Tests for string .toOctodecEqualDelimited() method - join words with 18 equals signs.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecEqualDelimited_basic(self):
        output = self._run('print("hello world".toOctodecEqualDelimited())')
        assert output[-1] == "hello" + "=" * 18 + "world"

    def test_toOctodecEqualDelimited_three(self):
        output = self._run('print("a b c".toOctodecEqualDelimited())')
        assert output[-1] == "a" + "=" * 18 + "b" + "=" * 18 + "c"
