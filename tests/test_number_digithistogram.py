"""
Tests for number .digitHistogram() method - sorted [digit, count] pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitHistogram:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitHistogram_basic(self):
        output = self._run('print(11223.digitHistogram())')
        assert output[-1] == "[[1, 2], [2, 2], [3, 1]]"

    def test_digitHistogram_single(self):
        output = self._run('print(5.digitHistogram())')
        assert output[-1] == "[[5, 1]]"
