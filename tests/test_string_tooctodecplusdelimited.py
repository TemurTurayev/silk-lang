"""
Tests for string .toOctodecPlusDelimited() method - join words with 18 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToOctodecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctodecPlusDelimited_basic(self):
        output = self._run('print("hello world".toOctodecPlusDelimited())')
        assert output[-1] == "hello" + "+" * 18 + "world"

    def test_toOctodecPlusDelimited_three(self):
        output = self._run('print("a b c".toOctodecPlusDelimited())')
        assert output[-1] == "a" + "+" * 18 + "b" + "+" * 18 + "c"
