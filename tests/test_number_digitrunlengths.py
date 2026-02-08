"""
Tests for number .digitRunLengths() method - run-length encoding of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitRunLengths:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitRunLengths_basic(self):
        output = self._run('print(11233.digitRunLengths())')
        assert output[-1] == "[[1, 2], [2, 1], [3, 2]]"

    def test_digitRunLengths_no_runs(self):
        output = self._run('print(123.digitRunLengths())')
        assert output[-1] == "[[1, 1], [2, 1], [3, 1]]"
