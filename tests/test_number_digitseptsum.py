"""
Tests for number .digitSeptSum() method - sum of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptSum_basic(self):
        output = self._run('print(12345671234567.digitSeptSum())')
        # [1+2+3+4+5+6+7=28, 1+2+3+4+5+6+7=28]
        assert output[-1] == "[28, 28]"

    def test_digitSeptSum_remainder(self):
        output = self._run('print(123456789.digitSeptSum())')
        # [1+2+3+4+5+6+7=28, 8+9=17]
        assert output[-1] == "[28, 17]"
