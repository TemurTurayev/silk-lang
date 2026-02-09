"""
Tests for number .digitTrigintSum() method - sum of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintSum_basic(self):
        output = self._run('print(111111111111111111111111111111.digitTrigintSum())')
        assert output[-1] == "[30]"

    def test_digitTrigintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111119.digitTrigintSum())')
        assert output[-1] == "[30, 9]"
