"""
Tests for number .digitAdjacentAvg() method - average of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentAvg_basic(self):
        output = self._run('print(152.digitAdjacentAvg())')
        # (1+5)/2, (5+2)/2 = [3, 3.5]
        assert output[-1] == "[3, 3.5]"

    def test_digitAdjacentAvg_even(self):
        output = self._run('print(2468.digitAdjacentAvg())')
        # (2+4)/2, (4+6)/2, (6+8)/2 = [3, 5, 7]
        assert output[-1] == "[3, 5, 7]"
