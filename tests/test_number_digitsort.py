"""
Tests for number .digitSort() method - sort digits ascending.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSort:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSort_basic(self):
        output = self._run('print(5312.digitSort())')
        assert output[-1] == "1235"

    def test_digitSort_repeated(self):
        output = self._run('print(9471.digitSort())')
        assert output[-1] == "1479"
