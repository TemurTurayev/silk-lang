"""
Tests for number .digitOctMin() method - min of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctMin_basic(self):
        output = self._run('print(1234567812345678.digitOctMin())')
        # [min(1..8)=1, min(1..8)=1]
        assert output[-1] == "[1, 1]"

    def test_digitOctMin_remainder(self):
        output = self._run('print(1234567890.digitOctMin())')
        # [min(1..8)=1, min(9,0)=0]
        assert output[-1] == "[1, 0]"
