"""
Tests for number .digitPairDiff() method - absolute diff of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairDiff:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairDiff_basic(self):
        output = self._run('print(1234.digitPairDiff())')
        # [|1-2|, |3-4|] = [1, 1]
        assert output[-1] == "[1, 1]"

    def test_digitPairDiff_odd(self):
        output = self._run('print(51627.digitPairDiff())')
        # [|5-1|, |6-2|, 7] = [4, 4, 7]
        assert output[-1] == "[4, 4, 7]"
