"""
Tests for string .toSeptendecEqualDelimited() method - join words with 17 equals signs.
"""

from silk.interpreter import Interpreter


class TestStringToSeptendecEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptendecEqualDelimited_basic(self):
        output = self._run('print("hello world".toSeptendecEqualDelimited())')
        assert output[-1] == "hello" + "=" * 17 + "world"

    def test_toSeptendecEqualDelimited_three(self):
        output = self._run('print("a b c".toSeptendecEqualDelimited())')
        assert output[-1] == "a" + "=" * 17 + "b" + "=" * 17 + "c"
