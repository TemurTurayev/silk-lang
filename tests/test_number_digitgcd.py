"""
Tests for number .digitGCD() method - GCD of all digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitGCD_basic(self):
        output = self._run('print(2468.digitGCD())')
        assert output[-1] == "2"

    def test_digitGCD_coprime(self):
        output = self._run('print(123.digitGCD())')
        assert output[-1] == "1"
