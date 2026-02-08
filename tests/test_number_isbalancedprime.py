"""
Tests for number .isBalancedPrime() method - prime equal to average of surrounding primes.
"""

from silk.interpreter import Interpreter


class TestNumberIsBalancedPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isBalancedPrime_5(self):
        output = self._run('print(5.isBalancedPrime())')
        assert output[-1] == "true"

    def test_isBalancedPrime_11(self):
        output = self._run('print(11.isBalancedPrime())')
        assert output[-1] == "false"
