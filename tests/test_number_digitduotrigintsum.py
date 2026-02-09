"""
Tests for number .digitDuotrigintSum() method - sum of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintSum_basic(self):
        output = self._run('print(11111111111111111111111111111111.digitDuotrigintSum())')
        assert output[-1] == "[32]"

    def test_digitDuotrigintSum_remainder(self):
        output = self._run('print(111111111111111111111111111111119.digitDuotrigintSum())')
        assert output[-1] == "[32, 9]"
