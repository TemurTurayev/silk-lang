"""
Tests for number .digitUnquadragintSum() method - sum of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintSum_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111.digitUnquadragintSum())')
        assert output[-1] == "[41]"

    def test_digitUnquadragintSum_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111115.digitUnquadragintSum())')
        assert output[-1] == "[41, 5]"
