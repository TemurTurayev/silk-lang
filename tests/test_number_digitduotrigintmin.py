"""
Tests for number .digitDuotrigintMin() method - min of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintMin_basic(self):
        output = self._run('print(22222222222222222222222222222222.digitDuotrigintMin())')
        assert output[-1] == "[2]"

    def test_digitDuotrigintMin_remainder(self):
        output = self._run('print(222222222222222222222222222222221.digitDuotrigintMin())')
        assert output[-1] == "[2, 1]"
