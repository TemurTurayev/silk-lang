"""
Tests for number .digitQuinquadragintMax() method - max of each consecutive 45-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinquadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinquadragintMax_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111.digitQuinquadragintMax())')
        assert output[-1] == "[1]"

    def test_digitQuinquadragintMax_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111119.digitQuinquadragintMax())')
        assert output[-1] == "[1, 9]"
