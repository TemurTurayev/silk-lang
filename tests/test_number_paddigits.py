"""
Tests for number .padDigits(n) method - pad with leading zeros.
"""

from silk.interpreter import Interpreter


class TestNumberPadDigits:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_padDigits_5(self):
        output = self._run('print(42.padDigits(5))')
        assert output[-1] == "00042"

    def test_padDigits_3(self):
        output = self._run('print(7.padDigits(3))')
        assert output[-1] == "007"
