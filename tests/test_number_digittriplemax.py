"""
Tests for number .digitTripleMax() method - max of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleMax_basic(self):
        output = self._run('print(123789.digitTripleMax())')
        # [max(1,2,3)=3, max(7,8,9)=9]
        assert output[-1] == "[3, 9]"

    def test_digitTripleMax_remainder(self):
        output = self._run('print(52847.digitTripleMax())')
        # [max(5,2,8)=8, max(4,7)=7]
        assert output[-1] == "[8, 7]"
