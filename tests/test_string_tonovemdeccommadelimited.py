"""
Tests for string .toNovemdecCommaDelimited() method - join words with 19 commas.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecCommaDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecCommaDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecCommaDelimited())')
        assert output[-1] == "hello" + "," * 19 + "world"

    def test_toNovemdecCommaDelimited_three(self):
        output = self._run('print("a b c".toNovemdecCommaDelimited())')
        assert output[-1] == "a" + "," * 19 + "b" + "," * 19 + "c"
