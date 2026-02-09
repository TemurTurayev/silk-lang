"""
Tests for number .digitQuattuorvigintAvg() method - avg of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintAvg_basic(self):
        output = self._run('print(111111111111111111111111.digitQuattuorvigintAvg())')
        assert output[-1] == "[1]"

    def test_digitQuattuorvigintAvg_remainder(self):
        output = self._run('print(1111111111111111111111115.digitQuattuorvigintAvg())')
        assert output[-1] == "[1, 5]"
