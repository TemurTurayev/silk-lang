"""
Tests for number .digitWindowLCM3() method - LCM of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowLCM3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowLCM3_basic(self):
        output = self._run('print(2346.digitWindowLCM3())')
        # lcm(2,3,4)=12, lcm(3,4,6)=12
        assert output[-1] == "[12, 12]"

    def test_digitWindowLCM3_primes(self):
        output = self._run('print(2357.digitWindowLCM3())')
        # lcm(2,3,5)=30, lcm(3,5,7)=105
        assert output[-1] == "[30, 105]"
