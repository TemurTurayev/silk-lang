"""
Tests for string .toDuovigintiPipeDelimited() method - join words with 22 pipe chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiPipeDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiPipeDelimited())')
        assert output[-1] == "hello" + "|" * 22 + "world"

    def test_toDuovigintiPipeDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiPipeDelimited())')
        assert output[-1] == "a" + "|" * 22 + "b" + "|" * 22 + "c"
