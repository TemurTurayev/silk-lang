"""
Tests for array .mapDigitAvg() method - average of digits of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitAvg_basic(self):
        output = self._run('print([12, 36, 5].mapDigitAvg())')
        # (1+2)/2=1.5, (3+6)/2=4.5, 5/1=5
        assert output[-1] == "[1.5, 4.5, 5]"

    def test_mapDigitAvg_integer(self):
        output = self._run('print([22, 33].mapDigitAvg())')
        # (2+2)/2=2, (3+3)/2=3
        assert output[-1] == "[2, 3]"
