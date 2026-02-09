"""
Tests for number .digitQuattuortrigintAvg() method - avg of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintAvg_basic(self):
        output = self._run('print(3333333333333333333333333333333333.digitQuattuortrigintAvg())')
        assert output[-1] == "[3]"

    def test_digitQuattuortrigintAvg_remainder(self):
        output = self._run('print(33333333333333333333333333333333336.digitQuattuortrigintAvg())')
        assert output[-1] == "[3, 6]"
