"""
Tests for number .digitTrequadragintLCM() method - LCM of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintLCM_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111.digitTrequadragintLCM())')
        assert output[-1] == "[1]"

    def test_digitTrequadragintLCM_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222222222344.digitTrequadragintLCM())')
        assert output[-1] == "[2, 12]"
