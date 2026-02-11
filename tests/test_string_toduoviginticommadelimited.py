"""
Tests for string .toDuovigintiCommaDelimited() method - join words with 22 commas.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiCommaDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiCommaDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiCommaDelimited())')
        assert output[-1] == "hello" + "," * 22 + "world"

    def test_toDuovigintiCommaDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiCommaDelimited())')
        assert output[-1] == "a" + "," * 22 + "b" + "," * 22 + "c"
