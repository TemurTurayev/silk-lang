"""
Tests for string .toTripleSemicolonDelimited() method - split words by ;;;.
"""

from silk.interpreter import Interpreter


class TestStringToTripleSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toTripleSemicolonDelimited())')
        assert output[-1] == "hello;;;world"

    def test_toTripleSemicolonDelimited_three(self):
        output = self._run('print("a b c".toTripleSemicolonDelimited())')
        assert output[-1] == "a;;;b;;;c"
