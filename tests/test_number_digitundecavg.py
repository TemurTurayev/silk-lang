"""
Tests for number .digitUndecAvg() method - average of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecAvg_basic(self):
        output = self._run('print(12345678901.digitUndecAvg())')
        # avg(1,2,3,4,5,6,7,8,9,0,1) = 46/11 = 4.181818...
        result = self._run('print(12345678901.digitUndecAvg())')
        val = result[-1]
        assert val.startswith("[4.1818")

    def test_digitUndecAvg_even(self):
        output = self._run('print(55555555555.digitUndecAvg())')
        # avg(5,5,5,5,5,5,5,5,5,5,5) = 5
        assert output[-1] == "[5]"
