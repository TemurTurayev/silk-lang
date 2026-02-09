"""
Tests for number .digitQuattuortrigintMax() method - max of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintMax_basic(self):
        output = self._run('print(3333333333333333333333333333333333.digitQuattuortrigintMax())')
        assert output[-1] == "[3]"

    def test_digitQuattuortrigintMax_remainder(self):
        output = self._run('print(33333333333333333333333333333333339.digitQuattuortrigintMax())')
        assert output[-1] == "[3, 9]"
