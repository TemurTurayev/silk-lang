"""
Tests for string .toQuindecPlusDelimited() method - join words with 15 plus signs.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecPlusDelimited_basic(self):
        output = self._run('print("hello world".toQuindecPlusDelimited())')
        assert output[-1] == "hello+++++++++++++++world"

    def test_toQuindecPlusDelimited_three(self):
        output = self._run('print("a b c".toQuindecPlusDelimited())')
        assert output[-1] == "a+++++++++++++++b+++++++++++++++c"
