"""
Tests for number .digitTripleMin() method - min of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleMin_basic(self):
        output = self._run('print(123789.digitTripleMin())')
        # [min(1,2,3)=1, min(7,8,9)=7]
        assert output[-1] == "[1, 7]"

    def test_digitTripleMin_remainder(self):
        output = self._run('print(52847.digitTripleMin())')
        # [min(5,2,8)=2, min(4,7)=4]
        assert output[-1] == "[2, 4]"
