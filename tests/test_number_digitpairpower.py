"""
Tests for number .digitPairPower() method - raise first digit to power of second in each pair.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairPower:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairPower_basic(self):
        output = self._run('print(2345.digitPairPower())')
        # [2^3=8, 4^5=1024]
        assert output[-1] == "[8, 1024]"

    def test_digitPairPower_odd(self):
        output = self._run('print(32147.digitPairPower())')
        # [3^2=9, 1^4=1, 7]
        assert output[-1] == "[9, 1, 7]"
