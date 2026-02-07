"""
Tests for array .runLengthEncode() method.
"""

from silk.interpreter import Interpreter


class TestArrayRunLengthEncode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_runLengthEncode_basic(self):
        output = self._run('print([1, 1, 2, 2, 2, 3].runLengthEncode())')
        assert output[-1] == "[[1, 2], [2, 3], [3, 1]]"

    def test_runLengthEncode_no_dupes(self):
        output = self._run('print([1, 2, 3].runLengthEncode())')
        assert output[-1] == "[[1, 1], [2, 1], [3, 1]]"

    def test_runLengthEncode_all_same(self):
        output = self._run('print([5, 5, 5].runLengthEncode())')
        assert output[-1] == "[[5, 3]]"
