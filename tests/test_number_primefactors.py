"""
Tests for number .primeFactors() method.
"""

from silk.interpreter import Interpreter


class TestNumberPrimeFactors:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_primeFactors_12(self):
        output = self._run('print(12.primeFactors())')
        assert output[-1] == "[2, 2, 3]"

    def test_primeFactors_prime(self):
        output = self._run('print(17.primeFactors())')
        assert output[-1] == "[17]"

    def test_primeFactors_100(self):
        output = self._run('print(100.primeFactors())')
        assert output[-1] == "[2, 2, 5, 5]"
