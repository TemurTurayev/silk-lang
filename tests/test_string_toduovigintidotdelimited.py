"""
Tests for string .toDuovigintiDotDelimited() method - join words with 22 dots.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiDotDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiDotDelimited())')
        assert output[-1] == "hello" + "." * 22 + "world"

    def test_toDuovigintiDotDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiDotDelimited())')
        assert output[-1] == "a" + "." * 22 + "b" + "." * 22 + "c"
