"""
Tests for number .digitTretrigintMin() method - min of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintMin_basic(self):
        output = self._run('print(222222222222222222222222222222222.digitTretrigintMin())')
        assert output[-1] == "[2]"

    def test_digitTretrigintMin_remainder(self):
        output = self._run('print(2222222222222222222222222222222221.digitTretrigintMin())')
        assert output[-1] == "[2, 1]"
