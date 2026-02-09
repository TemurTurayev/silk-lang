"""
Tests for number .digitSextrigintLCM() method - LCM of each consecutive 36-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextrigintLCM_basic(self):
        output = self._run('print(111111111111111111111111111111111111.digitSextrigintLCM())')
        assert output[-1] == "[1]"

    def test_digitSextrigintLCM_remainder(self):
        output = self._run('print(2222222222222222222222222222222222226.digitSextrigintLCM())')
        assert output[-1] == "[2, 6]"
