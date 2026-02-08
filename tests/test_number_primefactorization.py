"""
Tests for number .primeFactorization() method - list prime factors.
"""

from silk.interpreter import Interpreter


class TestNumberPrimeFactorization:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_primeFactorization_12(self):
        output = self._run('print(12.primeFactorization())')
        assert output[-1] == "[2, 2, 3]"

    def test_primeFactorization_30(self):
        output = self._run('print(30.primeFactorization())')
        assert output[-1] == "[2, 3, 5]"
