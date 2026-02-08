"""
Tests for number .digitTripleLCM() method - LCM of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleLCM_basic(self):
        output = self._run('print(234568.digitTripleLCM())')
        # [lcm(2,3,4)=12, lcm(5,6,8)=120]
        assert output[-1] == "[12, 120]"

    def test_digitTripleLCM_remainder(self):
        output = self._run('print(23456.digitTripleLCM())')
        # [lcm(2,3,4)=12, lcm(5,6)=30]
        assert output[-1] == "[12, 30]"
