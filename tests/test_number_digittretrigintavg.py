"""
Tests for number .digitTretrigintAvg() method - avg of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintAvg_basic(self):
        output = self._run('print(333333333333333333333333333333333.digitTretrigintAvg())')
        assert output[-1] == "[3]"

    def test_digitTretrigintAvg_remainder(self):
        output = self._run('print(3333333333333333333333333333333336.digitTretrigintAvg())')
        assert output[-1] == "[3, 6]"
