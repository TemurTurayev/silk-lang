"""
Tests for number .digitQuattuortrigintMin() method - min of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintMin_basic(self):
        output = self._run('print(2222222222222222222222222222222222.digitQuattuortrigintMin())')
        assert output[-1] == "[2]"

    def test_digitQuattuortrigintMin_remainder(self):
        output = self._run('print(22222222222222222222222222222222221.digitQuattuortrigintMin())')
        assert output[-1] == "[2, 1]"
