"""
Tests for number .digitSexvigintMin() method - min of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintMin_basic(self):
        output = self._run('print(11111111111111111111111111.digitSexvigintMin())')
        assert output[-1] == "[1]"

    def test_digitSexvigintMin_remainder(self):
        output = self._run('print(111111111111111111111111119.digitSexvigintMin())')
        assert output[-1] == "[1, 9]"
