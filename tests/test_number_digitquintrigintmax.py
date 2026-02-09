"""
Tests for number .digitQuintrigintMax() method - max of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintMax_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintMax())')
        assert output[-1] == "[1]"

    def test_digitQuintrigintMax_remainder(self):
        output = self._run('print(111111111111111111111111111111111119.digitQuintrigintMax())')
        assert output[-1] == "[1, 9]"
