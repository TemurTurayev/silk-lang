"""
Tests for string .toSextSemicolonDelimited() method - split words by ;;;;;;.
"""

from silk.interpreter import Interpreter


class TestStringToSextSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toSextSemicolonDelimited())')
        assert output[-1] == "hello;;;;;;world"

    def test_toSextSemicolonDelimited_three(self):
        output = self._run('print("a b c".toSextSemicolonDelimited())')
        assert output[-1] == "a;;;;;;b;;;;;;c"
