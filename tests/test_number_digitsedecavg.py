"""
Tests for number .digitSedecAvg() method - average of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecAvg_basic(self):
        output = self._run('print(1111111111111111.digitSedecAvg())')
        # avg(1*16) = 1.0
        assert output[-1] == "[1]"

    def test_digitSedecAvg_remainder(self):
        output = self._run('print(12345678123456785.digitSedecAvg())')
        # avg(1..8,1..8)=4.5, avg(5)=5.0
        assert output[-1] == "[4.5, 5]"
