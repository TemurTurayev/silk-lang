"""
Tests for number .digitSumEven() method - sum of even digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSumEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSumEven_basic(self):
        output = self._run('print(2468.digitSumEven())')
        assert output[-1] == "20"

    def test_digitSumEven_mixed(self):
        output = self._run('print(12345.digitSumEven())')
        # even digits: 2, 4 -> sum = 6
        assert output[-1] == "6"
