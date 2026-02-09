"""
Tests for string .toUndecPlusDelimited() method - split words by +++++++++++ (11 plus signs).
"""

from silk.interpreter import Interpreter


class TestStringToUndecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUndecPlusDelimited_basic(self):
        output = self._run('print("hello world".toUndecPlusDelimited())')
        assert output[-1] == "hello+++++++++++world"

    def test_toUndecPlusDelimited_three(self):
        output = self._run('print("a b c".toUndecPlusDelimited())')
        assert output[-1] == "a+++++++++++b+++++++++++c"
