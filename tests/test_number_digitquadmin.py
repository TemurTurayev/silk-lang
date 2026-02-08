"""
Tests for number .digitQuadMin() method - min of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadMin_basic(self):
        output = self._run('print(91845672.digitQuadMin())')
        # [min(9,1,8,4)=1, min(5,6,7,2)=2]
        assert output[-1] == "[1, 2]"

    def test_digitQuadMin_remainder(self):
        output = self._run('print(527463.digitQuadMin())')
        # [min(5,2,7,4)=2, min(6,3)=3]
        assert output[-1] == "[2, 3]"
