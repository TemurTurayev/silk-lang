"""
Tests for number .digitUntrigintMax() method - max of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintMax_basic(self):
        output = self._run('print(1111111111111111111111111111111.digitUntrigintMax())')
        assert output[-1] == "[1]"

    def test_digitUntrigintMax_remainder(self):
        output = self._run('print(11111111111111111111111111111119.digitUntrigintMax())')
        assert output[-1] == "[1, 9]"
