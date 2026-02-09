"""
Tests for number .digitQuintrigintMin() method - min of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintMin_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintMin())')
        assert output[-1] == "[1]"

    def test_digitQuintrigintMin_remainder(self):
        output = self._run('print(111111111111111111111111111111111110.digitQuintrigintMin())')
        assert output[-1] == "[1, 0]"
