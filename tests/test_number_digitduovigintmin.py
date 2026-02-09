"""
Tests for number .digitDuovigintMin() method - min of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintMin_basic(self):
        output = self._run('print(5555555555555555555555.digitDuovigintMin())')
        assert output[-1] == "[5]"

    def test_digitDuovigintMin_remainder(self):
        output = self._run('print(33333333333333333333332.digitDuovigintMin())')
        # min(3*22)=3, min(2)=2
        assert output[-1] == "[3, 2]"
