"""
Tests for string .toTripleAmpersandDelimited() method - split words by &&&.
"""

from silk.interpreter import Interpreter


class TestStringToTripleAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toTripleAmpersandDelimited())')
        assert output[-1] == "hello&&&world"

    def test_toTripleAmpersandDelimited_three(self):
        output = self._run('print("a b c".toTripleAmpersandDelimited())')
        assert output[-1] == "a&&&b&&&c"
