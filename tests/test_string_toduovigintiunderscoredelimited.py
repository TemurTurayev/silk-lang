"""
Tests for string .toDuovigintiUnderscoreDelimited() method - join words with 22 underscore chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiUnderscoreDelimited())')
        assert output[-1] == "hello" + "_" * 22 + "world"

    def test_toDuovigintiUnderscoreDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiUnderscoreDelimited())')
        assert output[-1] == "a" + "_" * 22 + "b" + "_" * 22 + "c"
