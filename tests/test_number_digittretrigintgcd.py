"""
Tests for number .digitTretrigintGCD() method - GCD of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintGCD_basic(self):
        output = self._run('print(444444444444444444444444444444444.digitTretrigintGCD())')
        assert output[-1] == "[4]"

    def test_digitTretrigintGCD_remainder(self):
        output = self._run('print(4444444444444444444444444444444446.digitTretrigintGCD())')
        assert output[-1] == "[4, 6]"
