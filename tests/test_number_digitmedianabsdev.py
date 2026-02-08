"""
Tests for number .digitMedianAbsDev() method - median absolute deviation of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMedianAbsDev:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMedianAbsDev_equal(self):
        output = self._run('print(333.digitMedianAbsDev())')
        assert output[-1] == "0"

    def test_digitMedianAbsDev_varied(self):
        output = self._run('print(135.digitMedianAbsDev())')
        # digits 1,3,5 => median=3, abs devs: 2,0,2 => median of devs = 2
        assert output[-1] == "2"
