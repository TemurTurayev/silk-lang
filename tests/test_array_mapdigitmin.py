"""
Tests for array .mapDigitMin() method - min digit of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitMin_basic(self):
        output = self._run('print([123, 456, 789].mapDigitMin())')
        assert output[-1] == "[1, 4, 7]"

    def test_mapDigitMin_withZero(self):
        output = self._run('print([102, 5, 930].mapDigitMin())')
        assert output[-1] == "[0, 5, 0]"
