"""
Tests for string .toSeptSemicolonDelimited() method - split words by ;;;;;;;.
"""

from silk.interpreter import Interpreter


class TestStringToSeptSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toSeptSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;;world"

    def test_toSeptSemicolonDelimited_three(self):
        output = self._run('print("a b c".toSeptSemicolonDelimited())')
        assert output[-1] == "a;;;;;;;b;;;;;;;c"
