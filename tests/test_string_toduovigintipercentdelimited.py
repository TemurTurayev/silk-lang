"""
Tests for string .toDuovigintiPercentDelimited() method - join words with 22 percent chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiPercentDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiPercentDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiPercentDelimited())')
        assert output[-1] == "hello" + "%" * 22 + "world"

    def test_toDuovigintiPercentDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiPercentDelimited())')
        assert output[-1] == "a" + "%" * 22 + "b" + "%" * 22 + "c"
