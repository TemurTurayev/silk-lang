"""
Tests for number .digitQuintrigintSum() method - sum of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintSum_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintSum())')
        assert output[-1] == "[35]"

    def test_digitQuintrigintSum_remainder(self):
        output = self._run('print(111111111111111111111111111111111115.digitQuintrigintSum())')
        assert output[-1] == "[35, 5]"
