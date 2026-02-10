"""
Tests for string .toUnvigintiEqualDelimited() method - join words with 21 equals signs.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiEqualDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiEqualDelimited())')
        assert output[-1] == "hello" + "=" * 21 + "world"

    def test_toUnvigintiEqualDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiEqualDelimited())')
        assert output[-1] == "a" + "=" * 21 + "b" + "=" * 21 + "c"
