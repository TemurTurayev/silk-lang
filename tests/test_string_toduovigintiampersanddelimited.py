"""
Tests for string .toDuovigintiAmpersandDelimited() method - join words with 22 ampersand chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 22 + "world"

    def test_toDuovigintiAmpersandDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 22 + "b" + "&" * 22 + "c"
