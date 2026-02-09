"""
Tests for number .digitDuotrigintMax() method - max of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintMax_basic(self):
        output = self._run('print(22222222222222222222222222222222.digitDuotrigintMax())')
        assert output[-1] == "[2]"

    def test_digitDuotrigintMax_remainder(self):
        output = self._run('print(222222222222222222222222222222229.digitDuotrigintMax())')
        assert output[-1] == "[2, 9]"
