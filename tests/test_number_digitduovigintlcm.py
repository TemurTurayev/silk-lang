"""
Tests for number .digitDuovigintLCM() method - LCM of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintLCM_basic(self):
        output = self._run('print(3333333333333333333333.digitDuovigintLCM())')
        assert output[-1] == "[3]"

    def test_digitDuovigintLCM_remainder(self):
        output = self._run('print(22222222222222222222224.digitDuovigintLCM())')
        # lcm(2*22)=2, lcm(4)=4
        assert output[-1] == "[2, 4]"
