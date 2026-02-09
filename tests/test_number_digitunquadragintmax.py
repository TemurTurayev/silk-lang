"""
Tests for number .digitUnquadragintMax() method - max of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintMax_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111.digitUnquadragintMax())')
        assert output[-1] == "[1]"

    def test_digitUnquadragintMax_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111119.digitUnquadragintMax())')
        assert output[-1] == "[1, 9]"
