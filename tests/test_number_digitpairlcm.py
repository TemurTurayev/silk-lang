"""
Tests for number .digitPairLCM() method - LCM of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairLCM_basic(self):
        output = self._run('print(4268.digitPairLCM())')
        # [lcm(4,2)=4, lcm(6,8)=24]
        assert output[-1] == "[4, 24]"

    def test_digitPairLCM_odd(self):
        output = self._run('print(93615.digitPairLCM())')
        # [lcm(9,3)=9, lcm(6,1)=6, 5]
        assert output[-1] == "[9, 6, 5]"
