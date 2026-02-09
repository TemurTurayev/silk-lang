"""
Tests for number .digitSedecSum() method - sum of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecSum_basic(self):
        output = self._run('print(1111111111111111.digitSedecSum())')
        # sum(1*16) = 16
        assert output[-1] == "[16]"

    def test_digitSedecSum_remainder(self):
        output = self._run('print(11111111111111119.digitSedecSum())')
        # sum(1*16)=16, sum(9)=9
        assert output[-1] == "[16, 9]"
