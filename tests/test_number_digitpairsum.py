"""
Tests for number .digitPairSum() method - sum of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairSum_basic(self):
        output = self._run('print(1234.digitPairSum())')
        # [1+2, 3+4] = [3, 7]
        assert output[-1] == "[3, 7]"

    def test_digitPairSum_odd(self):
        output = self._run('print(12345.digitPairSum())')
        # [1+2, 3+4, 5] = [3, 7, 5]
        assert output[-1] == "[3, 7, 5]"
