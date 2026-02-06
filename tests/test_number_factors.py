"""
Tests for number .factors() method.
"""

from silk.interpreter import Interpreter


class TestNumberFactors:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_factors_12(self):
        output = self._run('print(12.factors())')
        assert output[-1] == "[1, 2, 3, 4, 6, 12]"

    def test_factors_prime(self):
        output = self._run('print(7.factors())')
        assert output[-1] == "[1, 7]"

    def test_factors_one(self):
        output = self._run('print(1.factors())')
        assert output[-1] == "[1]"
