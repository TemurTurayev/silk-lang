"""
Tests for string .toTredecPlusDelimited() method - join words with 13 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToTredecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTredecPlusDelimited_basic(self):
        output = self._run('print("hello world".toTredecPlusDelimited())')
        assert output[-1] == "hello+++++++++++++world"

    def test_toTredecPlusDelimited_three(self):
        output = self._run('print("a b c".toTredecPlusDelimited())')
        assert output[-1] == "a+++++++++++++b+++++++++++++c"
