"""
Tests for number .digitQuattuorvigintSum() method - sum of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintSum_basic(self):
        output = self._run('print(111111111111111111111111.digitQuattuorvigintSum())')
        assert output[-1] == "[24]"

    def test_digitQuattuorvigintSum_remainder(self):
        output = self._run('print(1111111111111111111111113.digitQuattuorvigintSum())')
        # sum(1*24)=24, sum(3)=3
        assert output[-1] == "[24, 3]"
