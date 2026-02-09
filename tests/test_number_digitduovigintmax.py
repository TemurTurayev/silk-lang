"""
Tests for number .digitDuovigintMax() method - max of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintMax_basic(self):
        output = self._run('print(3333333333333333333333.digitDuovigintMax())')
        assert output[-1] == "[3]"

    def test_digitDuovigintMax_remainder(self):
        output = self._run('print(11111111111111111111119.digitDuovigintMax())')
        # max(1*22)=1, max(9)=9
        assert output[-1] == "[1, 9]"
