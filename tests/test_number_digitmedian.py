"""
Tests for number .digitMedian() method - median of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMedian:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMedian_odd(self):
        output = self._run('print(531.digitMedian())')
        assert output[-1] == "3"

    def test_digitMedian_even(self):
        output = self._run('print(1234.digitMedian())')
        assert output[-1] == "2.5"
