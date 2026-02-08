"""
Tests for number .digitQuintSum() method - sum of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintSum_basic(self):
        output = self._run('print(1234567890.digitQuintSum())')
        # [1+2+3+4+5=15, 6+7+8+9+0=30]
        assert output[-1] == "[15, 30]"

    def test_digitQuintSum_remainder(self):
        output = self._run('print(1234567.digitQuintSum())')
        # [1+2+3+4+5=15, 6+7=13]
        assert output[-1] == "[15, 13]"
