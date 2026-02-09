"""
Tests for number .digitQuinvigintMax() method - max of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintMax_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintMax())')
        assert output[-1] == "[1]"

    def test_digitQuinvigintMax_remainder(self):
        output = self._run('print(11111111111111111111111119.digitQuinvigintMax())')
        assert output[-1] == "[1, 9]"
