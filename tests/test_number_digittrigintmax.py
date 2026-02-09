"""
Tests for number .digitTrigintMax() method - max of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintMax_basic(self):
        output = self._run('print(111111111111111111111111111111.digitTrigintMax())')
        assert output[-1] == "[1]"

    def test_digitTrigintMax_remainder(self):
        output = self._run('print(1111111111111111111111111111119.digitTrigintMax())')
        assert output[-1] == "[1, 9]"
