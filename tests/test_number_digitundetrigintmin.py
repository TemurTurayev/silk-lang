"""
Tests for number .digitUndetrigintMin() method - min of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintMin_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintMin())')
        assert output[-1] == "[1]"

    def test_digitUndetrigintMin_remainder(self):
        output = self._run('print(111111111111111111111111111119.digitUndetrigintMin())')
        assert output[-1] == "[1, 9]"
