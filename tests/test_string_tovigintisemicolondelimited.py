"""
Tests for string .toVigintiSemicolonDelimited() method - join words with 20 semicolons.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiSemicolonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiSemicolonDelimited_basic(self):
        output = self._run('print("hello world".toVigintiSemicolonDelimited())')
        assert output[-1] == "hello" + ";" * 20 + "world"

    def test_toVigintiSemicolonDelimited_multi(self):
        output = self._run('print("a b c".toVigintiSemicolonDelimited())')
        assert output[-1] == "a" + ";" * 20 + "b" + ";" * 20 + "c"
