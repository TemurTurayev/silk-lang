"""
Tests for number .digitSeptentrigintLCM() method - LCM of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintLCM_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintLCM())')
        assert output[-1] == "[1]"

    def test_digitSeptentrigintLCM_remainder(self):
        output = self._run('print(22222222222222222222222222222222222226.digitSeptentrigintLCM())')
        assert output[-1] == "[2, 6]"
