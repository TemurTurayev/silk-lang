"""
Tests for number .digitUntrigintSum() method - sum of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintSum_basic(self):
        output = self._run('print(1111111111111111111111111111111.digitUntrigintSum())')
        assert output[-1] == "[31]"

    def test_digitUntrigintSum_remainder(self):
        output = self._run('print(11111111111111111111111111111119.digitUntrigintSum())')
        assert output[-1] == "[31, 9]"
