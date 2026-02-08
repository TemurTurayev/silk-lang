"""
Tests for number .digitAdjacentMax() method - max of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentMax_basic(self):
        output = self._run('print(152.digitAdjacentMax())')
        # max(1,5), max(5,2) = [5, 5]
        assert output[-1] == "[5, 5]"

    def test_digitAdjacentMax_ascending(self):
        output = self._run('print(1234.digitAdjacentMax())')
        # max(1,2), max(2,3), max(3,4) = [2, 3, 4]
        assert output[-1] == "[2, 3, 4]"
