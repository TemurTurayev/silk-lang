"""
Tests for number .digitUnvigintAvg() method - average of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintAvg_basic(self):
        output = self._run('print(111111111111111111111.digitUnvigintAvg())')
        assert output[-1] == "[1]"

    def test_digitUnvigintAvg_remainder(self):
        output = self._run('print(1111111111111111111119.digitUnvigintAvg())')
        # avg(1*21)=1, avg(9)=9
        assert output[-1] == "[1, 9]"
