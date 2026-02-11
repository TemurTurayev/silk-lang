"""
Tests for string .toUnvigintiUnderscoreDelimited() method - join words with 21 underscores.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiUnderscoreDelimited())')
        assert output[-1] == "hello" + "_" * 21 + "world"

    def test_toUnvigintiUnderscoreDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiUnderscoreDelimited())')
        assert output[-1] == "a" + "_" * 21 + "b" + "_" * 21 + "c"
