"""
Tests for string .toVigintiPlusDelimited() method - join words with 20 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiPlusDelimited_basic(self):
        output = self._run('print("hello world".toVigintiPlusDelimited())')
        assert output[-1] == "hello" + "+" * 20 + "world"

    def test_toVigintiPlusDelimited_multi(self):
        output = self._run('print("a b c".toVigintiPlusDelimited())')
        assert output[-1] == "a" + "+" * 20 + "b" + "+" * 20 + "c"
