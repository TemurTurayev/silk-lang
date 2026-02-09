"""
Tests for string .toQuattuordecPlusDelimited() method - join words with 14 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecPlusDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecPlusDelimited())')
        assert output[-1] == "hello++++++++++++++world"

    def test_toQuattuordecPlusDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecPlusDelimited())')
        assert output[-1] == "a++++++++++++++b++++++++++++++c"
