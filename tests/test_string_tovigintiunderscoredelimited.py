"""
Tests for string .toVigintiUnderscoreDelimited() method - join words with 20 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toVigintiUnderscoreDelimited())')
        assert output[-1] == "hello" + "_" * 20 + "world"

    def test_toVigintiUnderscoreDelimited_multi(self):
        output = self._run('print("a b c".toVigintiUnderscoreDelimited())')
        assert output[-1] == "a" + "_" * 20 + "b" + "_" * 20 + "c"
