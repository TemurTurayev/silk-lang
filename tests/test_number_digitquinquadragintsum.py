"""
Tests for number .digitQuinquadragintSum() method - sum of each consecutive 45-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinquadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinquadragintSum_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111.digitQuinquadragintSum())')
        assert output[-1] == "[45]"

    def test_digitQuinquadragintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111119.digitQuinquadragintSum())')
        assert output[-1] == "[45, 9]"
