"""
Tests for number .digitDuodetrigintSum() method - sum of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintSum_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintSum())')
        assert output[-1] == "[28]"

    def test_digitDuodetrigintSum_remainder(self):
        output = self._run('print(11111111111111111111111111115.digitDuodetrigintSum())')
        assert output[-1] == "[28, 5]"
