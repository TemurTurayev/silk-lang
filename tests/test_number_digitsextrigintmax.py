"""
Tests for number .digitSextrigintMax() method - max of each consecutive 36-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextrigintMax_basic(self):
        output = self._run('print(111111111111111111111111111111111111.digitSextrigintMax())')
        assert output[-1] == "[1]"

    def test_digitSextrigintMax_remainder(self):
        output = self._run('print(1111111111111111111111111111111111119.digitSextrigintMax())')
        assert output[-1] == "[1, 9]"
