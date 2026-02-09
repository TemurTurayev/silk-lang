"""
Tests for number .digitUnvigintLCM() method - LCM of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintLCM_basic(self):
        output = self._run('print(333333333333333333333.digitUnvigintLCM())')
        assert output[-1] == "[3]"

    def test_digitUnvigintLCM_remainder(self):
        output = self._run('print(2222222222222222222224.digitUnvigintLCM())')
        # lcm(2*21)=2, lcm(4)=4
        assert output[-1] == "[2, 4]"
