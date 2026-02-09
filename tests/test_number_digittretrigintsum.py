"""
Tests for number .digitTretrigintSum() method - sum of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintSum_basic(self):
        output = self._run('print(111111111111111111111111111111111.digitTretrigintSum())')
        assert output[-1] == "[33]"

    def test_digitTretrigintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111111115.digitTretrigintSum())')
        assert output[-1] == "[33, 5]"
