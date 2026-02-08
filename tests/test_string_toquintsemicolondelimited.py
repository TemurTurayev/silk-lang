"""
Tests for string .toQuintSemicolonDelimited() method - split words by ;;;;;.
"""

from silk.interpreter import Interpreter


class TestStringToQuintSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toQuintSemicolonDelimited())')
        assert output[-1] == "hello;;;;;world"

    def test_toQuintSemicolonDelimited_three(self):
        output = self._run('print("a b c".toQuintSemicolonDelimited())')
        assert output[-1] == "a;;;;;b;;;;;c"
