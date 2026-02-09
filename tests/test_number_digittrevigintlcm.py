"""
Tests for number .digitTrevigintLCM() method - LCM of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintLCM_basic(self):
        output = self._run('print(33333333333333333333333.digitTrevigintLCM())')
        assert output[-1] == "[3]"

    def test_digitTrevigintLCM_remainder(self):
        output = self._run('print(222222222222222222222224.digitTrevigintLCM())')
        # lcm(2*23)=2, lcm(4)=4
        assert output[-1] == "[2, 4]"
