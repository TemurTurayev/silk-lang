"""
Tests for number .digitQuadMax() method - max of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadMax_basic(self):
        output = self._run('print(12945678.digitQuadMax())')
        # [max(1,2,9,4)=9, max(5,6,7,8)=8]
        assert output[-1] == "[9, 8]"

    def test_digitQuadMax_remainder(self):
        output = self._run('print(527463.digitQuadMax())')
        # [max(5,2,7,4)=7, max(6,3)=6]
        assert output[-1] == "[7, 6]"
