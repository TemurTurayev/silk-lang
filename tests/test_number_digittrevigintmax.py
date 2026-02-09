"""
Tests for number .digitTrevigintMax() method - max of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintMax_basic(self):
        output = self._run('print(33333333333333333333333.digitTrevigintMax())')
        assert output[-1] == "[3]"

    def test_digitTrevigintMax_remainder(self):
        output = self._run('print(111111111111111111111119.digitTrevigintMax())')
        # max(1*23)=1, max(9)=9
        assert output[-1] == "[1, 9]"
