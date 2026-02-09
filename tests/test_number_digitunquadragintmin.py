"""
Tests for number .digitUnquadragintMin() method - min of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintMin_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111.digitUnquadragintMin())')
        assert output[-1] == "[1]"

    def test_digitUnquadragintMin_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111110.digitUnquadragintMin())')
        assert output[-1] == "[1, 0]"
