"""
Tests for number .digitVigintAvg() method - average of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintAvg_basic(self):
        output = self._run('print(11111111111111111111.digitVigintAvg())')
        assert output[-1] == "[1]"

    def test_digitVigintAvg_remainder(self):
        output = self._run('print(111111111111111111119.digitVigintAvg())')
        # avg(1*20)=1.0=1, avg(9)=9
        assert output[-1] == "[1, 9]"
