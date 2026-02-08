"""
Tests for number .isStrongPrime() method - prime greater than average of surrounding primes.
"""

from silk.interpreter import Interpreter


class TestNumberIsStrongPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isStrongPrime_11(self):
        output = self._run('print(11.isStrongPrime())')
        assert output[-1] == "true"

    def test_isStrongPrime_7(self):
        output = self._run('print(7.isStrongPrime())')
        assert output[-1] == "false"
