"""
Tests for number .digitQuattuorvigintMin() method - min of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintMin_basic(self):
        output = self._run('print(111111111111111111111111.digitQuattuorvigintMin())')
        assert output[-1] == "[1]"

    def test_digitQuattuorvigintMin_remainder(self):
        output = self._run('print(1111111111111111111111110.digitQuattuorvigintMin())')
        assert output[-1] == "[1, 0]"
