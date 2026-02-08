"""
Tests for number .digitSextSum() method - sum of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextSum_basic(self):
        output = self._run('print(123456789012.digitSextSum())')
        # [1+2+3+4+5+6=21, 7+8+9+0+1+2=27]
        assert output[-1] == "[21, 27]"

    def test_digitSextSum_remainder(self):
        output = self._run('print(12345678.digitSextSum())')
        # [1+2+3+4+5+6=21, 7+8=15]
        assert output[-1] == "[21, 15]"
