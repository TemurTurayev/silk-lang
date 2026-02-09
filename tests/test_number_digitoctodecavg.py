"""
Tests for number .digitOctodecAvg() method - average of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecAvg_basic(self):
        output = self._run('print(222222222222222222.digitOctodecAvg())')
        # avg(2,2,...,2) 18 twos = 2.0
        assert output[-1] == "[2]"

    def test_digitOctodecAvg_remainder(self):
        output = self._run('print(2222222222222222225.digitOctodecAvg())')
        # avg(18 twos)=2, avg(5)=5
        assert output[-1] == "[2, 5]"
