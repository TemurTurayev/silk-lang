"""
Tests for string .toDuovigintiStarDelimited() method - join words with 22 star chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiStarDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiStarDelimited())')
        assert output[-1] == "hello" + "*" * 22 + "world"

    def test_toDuovigintiStarDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiStarDelimited())')
        assert output[-1] == "a" + "*" * 22 + "b" + "*" * 22 + "c"
