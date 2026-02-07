"""
Tests for number .prevPrime() method.
"""

from silk.interpreter import Interpreter


class TestNumberPrevPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_prevPrime_from_10(self):
        output = self._run('print(10.prevPrime())')
        assert output[-1] == "7"

    def test_prevPrime_from_prime(self):
        output = self._run('print(7.prevPrime())')
        assert output[-1] == "5"

    def test_prevPrime_from_3(self):
        output = self._run('print(3.prevPrime())')
        assert output[-1] == "2"
