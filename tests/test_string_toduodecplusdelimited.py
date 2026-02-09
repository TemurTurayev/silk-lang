"""
Tests for string .toDuodecPlusDelimited() method - split words by ++++++++++++ (12 pluses).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecPlusDelimited_basic(self):
        output = self._run('print("hello world".toDuodecPlusDelimited())')
        assert output[-1] == "hello++++++++++++world"

    def test_toDuodecPlusDelimited_three(self):
        output = self._run('print("a b c".toDuodecPlusDelimited())')
        assert output[-1] == "a++++++++++++b++++++++++++c"
