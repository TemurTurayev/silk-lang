"""
Tests for string .toSemicolonDelimited() method - split words by semicolon.
"""

from silk.interpreter import Interpreter


class TestStringToSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toSemicolonDelimited())')
        assert output[-1] == "hello;world"

    def test_toSemicolonDelimited_three(self):
        output = self._run('print("a b c".toSemicolonDelimited())')
        assert output[-1] == "a;b;c"
