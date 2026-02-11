"""
Tests for string .toUnvigintiPlusDelimited() method - join words with 21 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiPlusDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiPlusDelimited())')
        assert output[-1] == "hello" + "+" * 21 + "world"

    def test_toUnvigintiPlusDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiPlusDelimited())')
        assert output[-1] == "a" + "+" * 21 + "b" + "+" * 21 + "c"
