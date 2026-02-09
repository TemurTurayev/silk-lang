"""
Tests for string .toOctodecCommaDelimited() method - join words with 18 commas.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecCommaDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecCommaDelimited_basic(self):
        output = self._run('print("hello world".toOctodecCommaDelimited())')
        assert output[-1] == "hello" + "," * 18 + "world"

    def test_toOctodecCommaDelimited_three(self):
        output = self._run('print("a b c".toOctodecCommaDelimited())')
        assert output[-1] == "a" + "," * 18 + "b" + "," * 18 + "c"
