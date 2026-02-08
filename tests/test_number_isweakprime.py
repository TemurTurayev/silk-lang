"""
Tests for number .isWeakPrime() method - prime less than average of surrounding primes.
"""

from silk.interpreter import Interpreter


class TestNumberIsWeakPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isWeakPrime_13(self):
        output = self._run('print(13.isWeakPrime())')
        assert output[-1] == "true"

    def test_isWeakPrime_11(self):
        output = self._run('print(11.isWeakPrime())')
        assert output[-1] == "false"
