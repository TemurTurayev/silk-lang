"""
Tests for number .digitPowerSum() method - sum of each digit raised to its own value.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPowerSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPowerSum_basic(self):
        output = self._run('print(123.digitPowerSum())')
        assert output[-1] == "32"

    def test_digitPowerSum_single(self):
        output = self._run('print(5.digitPowerSum())')
        assert output[-1] == "3125"
