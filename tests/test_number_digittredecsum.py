"""
Tests for number .digitTredecSum() method - sum of each consecutive 13-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTredecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTredecSum_basic(self):
        output = self._run('print(1234567890123.digitTredecSum())')
        # sum(1,2,3,4,5,6,7,8,9,0,1,2,3) = 51
        assert output[-1] == "[51]"

    def test_digitTredecSum_remainder(self):
        output = self._run('print(12345678901235.digitTredecSum())')
        # sum(1..3)=51, sum(5)=5
        assert output[-1] == "[51, 5]"
