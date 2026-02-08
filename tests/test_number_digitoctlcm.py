"""
Tests for number .digitOctLCM() method - LCM of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctLCM_basic(self):
        output = self._run('print(1234567812345678.digitOctLCM())')
        # [lcm(1,2,3,4,5,6,7,8)=840, lcm(1,2,3,4,5,6,7,8)=840]
        assert output[-1] == "[840, 840]"

    def test_digitOctLCM_remainder(self):
        output = self._run('print(1234567893.digitOctLCM())')
        # [lcm(1,2,3,4,5,6,7,8)=840, lcm(9,3)=9]
        assert output[-1] == "[840, 9]"
