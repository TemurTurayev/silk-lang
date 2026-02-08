"""
Tests for number .digitAdjacentSum() method - sum of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentSum_basic(self):
        output = self._run('print(123.digitAdjacentSum())')
        # (1+2) + (2+3) = 3 + 5 = 8
        assert output[-1] == "[3, 5]"

    def test_digitAdjacentSum_four(self):
        output = self._run('print(1234.digitAdjacentSum())')
        # (1+2) + (2+3) + (3+4) = [3, 5, 7]
        assert output[-1] == "[3, 5, 7]"
