"""
Tests for number .digitTretrigintMax() method - max of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintMax_basic(self):
        output = self._run('print(222222222222222222222222222222222.digitTretrigintMax())')
        assert output[-1] == "[2]"

    def test_digitTretrigintMax_remainder(self):
        output = self._run('print(2222222222222222222222222222222229.digitTretrigintMax())')
        assert output[-1] == "[2, 9]"
