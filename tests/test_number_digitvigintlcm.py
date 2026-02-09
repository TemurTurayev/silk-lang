"""
Tests for number .digitVigintLCM() method - LCM of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintLCM_basic(self):
        output = self._run('print(33333333333333333333.digitVigintLCM())')
        assert output[-1] == "[3]"

    def test_digitVigintLCM_remainder(self):
        output = self._run('print(222222222222222222224.digitVigintLCM())')
        # lcm(2*20)=2, lcm(4)=4
        assert output[-1] == "[2, 4]"
