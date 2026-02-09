"""
Tests for number .digitTrevigintMin() method - min of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintMin_basic(self):
        output = self._run('print(55555555555555555555555.digitTrevigintMin())')
        assert output[-1] == "[5]"

    def test_digitTrevigintMin_remainder(self):
        output = self._run('print(333333333333333333333332.digitTrevigintMin())')
        # min(3*23)=3, min(2)=2
        assert output[-1] == "[3, 2]"
