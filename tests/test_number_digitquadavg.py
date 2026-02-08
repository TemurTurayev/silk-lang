"""
Tests for number .digitQuadAvg() method - average of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadAvg_basic(self):
        output = self._run('print(12345678.digitQuadAvg())')
        # [avg(1,2,3,4)=2.5, avg(5,6,7,8)=6.5]
        assert output[-1] == "[2.5, 6.5]"

    def test_digitQuadAvg_remainder(self):
        output = self._run('print(246813.digitQuadAvg())')
        # [avg(2,4,6,8)=5, avg(1,3)=2]
        assert output[-1] == "[5, 2]"
