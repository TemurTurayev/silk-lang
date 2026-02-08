"""
Tests for array .mapDigitSum() method - sum of digits of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitSum_basic(self):
        output = self._run('print([12, 34, 56].mapDigitSum())')
        assert output[-1] == "[3, 7, 11]"

    def test_mapDigitSum_single(self):
        output = self._run('print([5, 9, 100].mapDigitSum())')
        assert output[-1] == "[5, 9, 1]"
