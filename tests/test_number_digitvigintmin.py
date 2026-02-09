"""
Tests for number .digitVigintMin() method - min of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintMin_basic(self):
        output = self._run('print(12111211121112111211.digitVigintMin())')
        assert output[-1] == "[1]"

    def test_digitVigintMin_remainder(self):
        output = self._run('print(121112111211121112119.digitVigintMin())')
        # min(...)=1, min(9)=9
        assert output[-1] == "[1, 9]"
