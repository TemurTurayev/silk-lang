"""
Tests for number .star() method - star number 6*n*(n-1)+1.
"""

from silk.interpreter import Interpreter


class TestNumberStar:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_star_1(self):
        output = self._run('print(1.star())')
        assert output[-1] == "1"

    def test_star_3(self):
        output = self._run('print(3.star())')
        assert output[-1] == "37"

    def test_star_4(self):
        output = self._run('print(4.star())')
        assert output[-1] == "73"
