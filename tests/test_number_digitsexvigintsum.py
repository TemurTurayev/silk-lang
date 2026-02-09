"""
Tests for number .digitSexvigintSum() method - sum of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintSum_basic(self):
        output = self._run('print(11111111111111111111111111.digitSexvigintSum())')
        assert output[-1] == "[26]"

    def test_digitSexvigintSum_remainder(self):
        output = self._run('print(111111111111111111111111113.digitSexvigintSum())')
        assert output[-1] == "[26, 3]"
