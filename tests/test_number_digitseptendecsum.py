"""
Tests for number .digitSeptendecSum() method - sum of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecSum_basic(self):
        output = self._run('print(11111111111111111.digitSeptendecSum())')
        # sum(1*17) = 17
        assert output[-1] == "[17]"

    def test_digitSeptendecSum_remainder(self):
        output = self._run('print(111111111111111119.digitSeptendecSum())')
        # sum(1*17)=17, sum(9)=9
        assert output[-1] == "[17, 9]"
