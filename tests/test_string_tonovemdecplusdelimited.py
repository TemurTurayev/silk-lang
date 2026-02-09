"""
Tests for string .toNovemdecPlusDelimited() method - join words with 19 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToNovemdecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNovemdecPlusDelimited_basic(self):
        output = self._run('print("hello world".toNovemdecPlusDelimited())')
        assert output[-1] == "hello" + "+" * 19 + "world"

    def test_toNovemdecPlusDelimited_three(self):
        output = self._run('print("a b c".toNovemdecPlusDelimited())')
        assert output[-1] == "a" + "+" * 19 + "b" + "+" * 19 + "c"
