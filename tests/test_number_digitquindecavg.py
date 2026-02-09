"""
Tests for number .digitQuindecAvg() method - average of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecAvg_basic(self):
        output = self._run('print(123456789012345.digitQuindecAvg())')
        # avg(1..5,6..9,0,1..5) = 60/15 = 4
        assert output[-1] == "[4]"

    def test_digitQuindecAvg_remainder(self):
        output = self._run('print(1234567890123457.digitQuindecAvg())')
        result = eval(output[-1])
        assert result[1] == 7
