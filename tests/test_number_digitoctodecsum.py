"""
Tests for number .digitOctodecSum() method - sum of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecSum_basic(self):
        output = self._run('print(111111111111111111.digitOctodecSum())')
        # sum(1*18) = 18
        assert output[-1] == "[18]"

    def test_digitOctodecSum_remainder(self):
        output = self._run('print(1111111111111111119.digitOctodecSum())')
        # sum(1*18)=18, sum(9)=9
        assert output[-1] == "[18, 9]"
