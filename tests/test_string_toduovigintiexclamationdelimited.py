"""
Tests for string .toDuovigintiExclamationDelimited() method - join words with 22 exclamation chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiExclamationDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiExclamationDelimited())')
        assert output[-1] == "hello" + "!" * 22 + "world"

    def test_toDuovigintiExclamationDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiExclamationDelimited())')
        assert output[-1] == "a" + "!" * 22 + "b" + "!" * 22 + "c"
