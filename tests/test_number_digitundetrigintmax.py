"""
Tests for number .digitUndetrigintMax() method - max of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintMax_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintMax())')
        assert output[-1] == "[1]"

    def test_digitUndetrigintMax_remainder(self):
        output = self._run('print(111111111111111111111111111119.digitUndetrigintMax())')
        assert output[-1] == "[1, 9]"
