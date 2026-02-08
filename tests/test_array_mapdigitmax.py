"""
Tests for array .mapDigitMax() method - max digit of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitMax_basic(self):
        output = self._run('print([123, 456, 789].mapDigitMax())')
        assert output[-1] == "[3, 6, 9]"

    def test_mapDigitMax_same(self):
        output = self._run('print([111, 5, 902].mapDigitMax())')
        assert output[-1] == "[1, 5, 9]"
