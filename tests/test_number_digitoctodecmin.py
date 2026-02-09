"""
Tests for number .digitOctodecMin() method - min of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecMin_basic(self):
        output = self._run('print(121112111211121112.digitOctodecMin())')
        # min(1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2) = 1
        assert output[-1] == "[1]"

    def test_digitOctodecMin_remainder(self):
        output = self._run('print(1211121112111211129.digitOctodecMin())')
        # min(...)=1, min(9)=9
        assert output[-1] == "[1, 9]"
