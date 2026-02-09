"""
Tests for number .digitSextrigintMin() method - min of each consecutive 36-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextrigintMin_basic(self):
        output = self._run('print(111111111111111111111111111111111111.digitSextrigintMin())')
        assert output[-1] == "[1]"

    def test_digitSextrigintMin_remainder(self):
        output = self._run('print(1111111111111111111111111111111111110.digitSextrigintMin())')
        assert output[-1] == "[1, 0]"
