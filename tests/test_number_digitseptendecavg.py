"""
Tests for number .digitSeptendecAvg() method - average of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecAvg_basic(self):
        output = self._run('print(11111111111111111.digitSeptendecAvg())')
        # avg(1*17) = 1.0
        assert output[-1] == "[1]"

    def test_digitSeptendecAvg_remainder(self):
        output = self._run('print(222222222222222225.digitSeptendecAvg())')
        # avg(2*17)=2.0, avg(5)=5.0
        assert output[-1] == "[2, 5]"
