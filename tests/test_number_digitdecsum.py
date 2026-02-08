"""
Tests for number .digitDecSum() method - sum of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecSum_basic(self):
        output = self._run('print(12345678901234567890.digitDecSum())')
        # [1+2+3+4+5+6+7+8+9+0=45, 1+2+3+4+5+6+7+8+9+0=45]
        assert output[-1] == "[45, 45]"

    def test_digitDecSum_remainder(self):
        output = self._run('print(123456789012.digitDecSum())')
        # [1+2+3+4+5+6+7+8+9+0=45, 1+2=3]
        assert output[-1] == "[45, 3]"
