"""
Tests for number .digitDuoquadragintSum() method - sum of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintSum_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111.digitDuoquadragintSum())')
        assert output[-1] == "[42]"

    def test_digitDuoquadragintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111119.digitDuoquadragintSum())')
        assert output[-1] == "[42, 9]"
