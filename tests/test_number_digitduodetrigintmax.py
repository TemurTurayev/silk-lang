"""
Tests for number .digitDuodetrigintMax() method - max of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintMax_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintMax())')
        assert output[-1] == "[1]"

    def test_digitDuodetrigintMax_remainder(self):
        output = self._run('print(11111111111111111111111111119.digitDuodetrigintMax())')
        assert output[-1] == "[1, 9]"
