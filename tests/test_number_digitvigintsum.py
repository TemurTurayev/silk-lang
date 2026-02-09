"""
Tests for number .digitVigintSum() method - sum of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintSum_basic(self):
        output = self._run('print(11111111111111111111.digitVigintSum())')
        # sum(1*20) = 20
        assert output[-1] == "[20]"

    def test_digitVigintSum_remainder(self):
        output = self._run('print(111111111111111111115.digitVigintSum())')
        # sum(20 ones)=20, sum(5)=5
        assert output[-1] == "[20, 5]"
