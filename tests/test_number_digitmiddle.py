"""
Tests for number .digitMiddle() method - return middle digit of odd-length number.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMiddle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMiddle_basic(self):
        output = self._run('print(12345.digitMiddle())')
        assert output[-1] == "3"

    def test_digitMiddle_single(self):
        output = self._run('print(7.digitMiddle())')
        assert output[-1] == "7"
