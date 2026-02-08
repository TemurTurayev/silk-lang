"""
Tests for number .digitInterquartileRange() method - IQR of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitInterquartileRange:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitInterquartileRange_equal(self):
        output = self._run('print(3333.digitInterquartileRange())')
        assert output[-1] == "0"

    def test_digitInterquartileRange_varied(self):
        output = self._run('print(1234.digitInterquartileRange())')
        # sorted: 1,2,3,4 => Q1=1.5, Q3=3.5, IQR=2
        assert output[-1] == "2"
