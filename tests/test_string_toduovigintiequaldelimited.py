"""
Tests for string .toDuovigintiEqualDelimited() method - join words with 22 equal signs.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiEqualDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiEqualDelimited())')
        assert output[-1] == "hello" + "=" * 22 + "world"

    def test_toDuovigintiEqualDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiEqualDelimited())')
        assert output[-1] == "a" + "=" * 22 + "b" + "=" * 22 + "c"
