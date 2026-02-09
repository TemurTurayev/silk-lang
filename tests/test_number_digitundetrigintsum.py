"""
Tests for number .digitUndetrigintSum() method - sum of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintSum_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintSum())')
        assert output[-1] == "[29]"

    def test_digitUndetrigintSum_remainder(self):
        output = self._run('print(111111111111111111111111111119.digitUndetrigintSum())')
        assert output[-1] == "[29, 9]"
