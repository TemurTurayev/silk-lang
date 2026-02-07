"""
Tests for number .tetrahedral() method - tetrahedral number n*(n+1)*(n+2)/6.
"""

from silk.interpreter import Interpreter


class TestNumberTetrahedral:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_tetrahedral_1(self):
        output = self._run('print(1.tetrahedral())')
        assert output[-1] == "1"

    def test_tetrahedral_4(self):
        output = self._run('print(4.tetrahedral())')
        assert output[-1] == "20"

    def test_tetrahedral_5(self):
        output = self._run('print(5.tetrahedral())')
        assert output[-1] == "35"
