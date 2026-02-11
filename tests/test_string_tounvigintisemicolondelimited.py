"""
Tests for string .toUnvigintiSemicolonDelimited() method - join words with 21 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiSemicolonDelimited())')
        assert output[-1] == "hello" + ";" * 21 + "world"

    def test_toUnvigintiSemicolonDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiSemicolonDelimited())')
        assert output[-1] == "a" + ";" * 21 + "b" + ";" * 21 + "c"
