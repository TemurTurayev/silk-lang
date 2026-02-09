"""
Tests for number .digitQuattuorvigintMax() method - max of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintMax_basic(self):
        output = self._run('print(111111111111111111111111.digitQuattuorvigintMax())')
        assert output[-1] == "[1]"

    def test_digitQuattuorvigintMax_remainder(self):
        output = self._run('print(1111111111111111111111119.digitQuattuorvigintMax())')
        assert output[-1] == "[1, 9]"
