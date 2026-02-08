"""
Tests for number .digitQuintMin() method - min of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintMin_basic(self):
        output = self._run('print(1234567890.digitQuintMin())')
        # [min(1,2,3,4,5)=1, min(6,7,8,9,0)=0]
        assert output[-1] == "[1, 0]"

    def test_digitQuintMin_remainder(self):
        output = self._run('print(5432198.digitQuintMin())')
        # [min(5,4,3,2,1)=1, min(9,8)=8]
        assert output[-1] == "[1, 8]"
