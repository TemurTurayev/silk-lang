"""
Tests for string .toDuovigintiPlusDelimited() method - join words with 22 plus chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiPlusDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiPlusDelimited())')
        assert output[-1] == "hello" + "+" * 22 + "world"

    def test_toDuovigintiPlusDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiPlusDelimited())')
        assert output[-1] == "a" + "+" * 22 + "b" + "+" * 22 + "c"
