"""
Tests for string .toOctodecAmpersandDelimited() method - join words with 18 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toOctodecAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 18 + "world"

    def test_toOctodecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toOctodecAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 18 + "b" + "&" * 18 + "c"
