"""
Tests for string .toSedecPlusDelimited() method - join words with 16 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToSedecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecPlusDelimited_basic(self):
        output = self._run('print("hello world".toSedecPlusDelimited())')
        assert output[-1] == "hello" + "+" * 16 + "world"

    def test_toSedecPlusDelimited_three(self):
        output = self._run('print("a b c".toSedecPlusDelimited())')
        assert output[-1] == "a" + "+" * 16 + "b" + "+" * 16 + "c"
