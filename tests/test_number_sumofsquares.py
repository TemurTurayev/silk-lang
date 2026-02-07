"""
Tests for number .sumOfSquares() method.
"""

from silk.interpreter import Interpreter


class TestNumberSumOfSquares:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sumOfSquares_basic(self):
        output = self._run('print(3.sumOfSquares())')
        assert output[-1] == "14"

    def test_sumOfSquares_one(self):
        output = self._run('print(1.sumOfSquares())')
        assert output[-1] == "1"
