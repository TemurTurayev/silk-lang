"""
Tests for number .primesBetween(max) method - list primes from n to max.
"""

from silk.interpreter import Interpreter


class TestNumberPrimesBetween:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_primesBetween_10_20(self):
        output = self._run('print(10.primesBetween(20))')
        assert output[-1] == "[11, 13, 17, 19]"

    def test_primesBetween_1_10(self):
        output = self._run('print(1.primesBetween(10))')
        assert output[-1] == "[2, 3, 5, 7]"
