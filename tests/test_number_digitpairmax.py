"""
Tests for number .digitPairMax() method - max of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairMax_basic(self):
        output = self._run('print(1234.digitPairMax())')
        # [max(1,2), max(3,4)] = [2, 4]
        assert output[-1] == "[2, 4]"

    def test_digitPairMax_odd(self):
        output = self._run('print(51627.digitPairMax())')
        # [max(5,1), max(6,2), 7] = [5, 6, 7]
        assert output[-1] == "[5, 6, 7]"
