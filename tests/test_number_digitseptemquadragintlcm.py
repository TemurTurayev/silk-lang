"""
Tests for number .digitSeptemquadragintLCM() method - LCM of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintLCM_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintLCM())')
        assert output[-1] == "[1]"

    def test_digitSeptemquadragintLCM_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222222222226.digitSeptemquadragintLCM())')
        assert output[-1] == "[2, 6]"
