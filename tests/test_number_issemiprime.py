"""
Tests for number .isSemiPrime() method - product of exactly 2 primes.
"""

from silk.interpreter import Interpreter


class TestNumberIsSemiPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSemiPrime_6(self):
        output = self._run('print(6.isSemiPrime())')
        assert output[-1] == "true"

    def test_isSemiPrime_4(self):
        output = self._run('print(4.isSemiPrime())')
        assert output[-1] == "true"

    def test_isSemiPrime_12(self):
        output = self._run('print(12.isSemiPrime())')
        assert output[-1] == "false"
