"""
Tests for number .digitAdjacentMin() method - min of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentMin_basic(self):
        output = self._run('print(152.digitAdjacentMin())')
        # min(1,5), min(5,2) = [1, 2]
        assert output[-1] == "[1, 2]"

    def test_digitAdjacentMin_ascending(self):
        output = self._run('print(1234.digitAdjacentMin())')
        # min(1,2), min(2,3), min(3,4) = [1, 2, 3]
        assert output[-1] == "[1, 2, 3]"
