"""
Tests for number .digitSexquadragintLCM() method - LCM of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintLCM_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintLCM())')
        assert output[-1] == "[1]"

    def test_digitSexquadragintLCM_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222222222226.digitSexquadragintLCM())')
        assert output[-1] == "[2, 6]"
