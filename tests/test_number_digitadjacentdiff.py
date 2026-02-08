"""
Tests for number .digitAdjacentDiff() method - absolute diff of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentDiff:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentDiff_basic(self):
        output = self._run('print(152.digitAdjacentDiff())')
        # |1-5|, |5-2| = [4, 3]
        assert output[-1] == "[4, 3]"

    def test_digitAdjacentDiff_ascending(self):
        output = self._run('print(1234.digitAdjacentDiff())')
        # |1-2|, |2-3|, |3-4| = [1, 1, 1]
        assert output[-1] == "[1, 1, 1]"
