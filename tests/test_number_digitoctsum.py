"""
Tests for number .digitOctSum() method - sum of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctSum_basic(self):
        output = self._run('print(1234567812345678.digitOctSum())')
        # [1+2+3+4+5+6+7+8=36, 1+2+3+4+5+6+7+8=36]
        assert output[-1] == "[36, 36]"

    def test_digitOctSum_remainder(self):
        output = self._run('print(1234567890.digitOctSum())')
        # [1+2+3+4+5+6+7+8=36, 9+0=9]
        assert output[-1] == "[36, 9]"
