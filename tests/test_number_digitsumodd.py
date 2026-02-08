"""
Tests for number .digitSumOdd() method - sum of odd digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSumOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSumOdd_allOdd(self):
        output = self._run('print(1357.digitSumOdd())')
        assert output[-1] == "16"

    def test_digitSumOdd_mixed(self):
        output = self._run('print(12345.digitSumOdd())')
        # odd digits: 1, 3, 5 -> sum = 9
        assert output[-1] == "9"
