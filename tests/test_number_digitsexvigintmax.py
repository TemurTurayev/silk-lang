"""
Tests for number .digitSexvigintMax() method - max of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintMax_basic(self):
        output = self._run('print(11111111111111111111111111.digitSexvigintMax())')
        assert output[-1] == "[1]"

    def test_digitSexvigintMax_remainder(self):
        output = self._run('print(111111111111111111111111119.digitSexvigintMax())')
        assert output[-1] == "[1, 9]"
