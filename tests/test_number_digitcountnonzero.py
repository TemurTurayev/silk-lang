"""
Tests for number .digitCountNonZero() method - count non-zero digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCountNonZero:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCountNonZero_all(self):
        output = self._run('print(123.digitCountNonZero())')
        assert output[-1] == "3"

    def test_digitCountNonZero_withZeros(self):
        output = self._run('print(10203.digitCountNonZero())')
        assert output[-1] == "3"
