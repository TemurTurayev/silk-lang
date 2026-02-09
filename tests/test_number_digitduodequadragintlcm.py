"""
Tests for number .digitDuodequadragintLCM() method - LCM of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintLCM_basic(self):
        output = self._run('print(22222222222222222222222222222222222222.digitDuodequadragintLCM())')
        assert output[-1] == "[2]"

    def test_digitDuodequadragintLCM_remainder(self):
        output = self._run('print(222222222222222222222222222222222222223.digitDuodequadragintLCM())')
        assert output[-1] == "[2, 3]"
