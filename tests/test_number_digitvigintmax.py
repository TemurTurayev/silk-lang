"""
Tests for number .digitVigintMax() method - max of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintMax_basic(self):
        output = self._run('print(12111211121112111211.digitVigintMax())')
        # max digits = 2
        assert output[-1] == "[2]"

    def test_digitVigintMax_remainder(self):
        output = self._run('print(121112111211121112119.digitVigintMax())')
        # max(...)=2, max(9)=9
        assert output[-1] == "[2, 9]"
