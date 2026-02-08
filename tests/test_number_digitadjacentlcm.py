"""
Tests for number .digitAdjacentLCM() method - LCM of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentLCM_basic(self):
        output = self._run('print(264.digitAdjacentLCM())')
        # lcm(2,6), lcm(6,4) = [6, 12]
        assert output[-1] == "[6, 12]"

    def test_digitAdjacentLCM_coprimes(self):
        output = self._run('print(357.digitAdjacentLCM())')
        # lcm(3,5), lcm(5,7) = [15, 35]
        assert output[-1] == "[15, 35]"
