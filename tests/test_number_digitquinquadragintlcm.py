"""
Tests for number .digitQuinquadragintLCM() method - LCM of each consecutive 45-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinquadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinquadragintLCM_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111.digitQuinquadragintLCM())')
        assert output[-1] == "[1]"

    def test_digitQuinquadragintLCM_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222222222344.digitQuinquadragintLCM())')
        assert output[-1] == "[2, 12]"
