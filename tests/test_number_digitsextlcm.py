"""
Tests for number .digitSextLCM() method - LCM of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextLCM_basic(self):
        output = self._run('print(123612123612.digitSextLCM())')
        # [lcm(1,2,3,6,1,2)=6, lcm(1,2,3,6,1,2)=6]
        assert output[-1] == "[6, 6]"

    def test_digitSextLCM_remainder(self):
        output = self._run('print(12361236.digitSextLCM())')
        # [lcm(1,2,3,6,1,2)=6, lcm(3,6)=6]
        assert output[-1] == "[6, 6]"
