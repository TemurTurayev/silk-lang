"""
Tests for number .digitQuintLCM() method - LCM of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintLCM_basic(self):
        output = self._run('print(1234612346.digitQuintLCM())')
        # [lcm(1,2,3,4,6)=12, lcm(1,2,3,4,6)=12]
        assert output[-1] == "[12, 12]"

    def test_digitQuintLCM_remainder(self):
        output = self._run('print(1234636.digitQuintLCM())')
        # [lcm(1,2,3,4,6)=12, lcm(3,6)=6]
        assert output[-1] == "[12, 6]"
