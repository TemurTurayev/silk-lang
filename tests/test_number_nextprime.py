"""
Tests for number .nextPrime() method.
"""

from silk.interpreter import Interpreter


class TestNumberNextPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_nextPrime_from_10(self):
        output = self._run('print(10.nextPrime())')
        assert output[-1] == "11"

    def test_nextPrime_from_prime(self):
        output = self._run('print(7.nextPrime())')
        assert output[-1] == "11"

    def test_nextPrime_from_1(self):
        output = self._run('print(1.nextPrime())')
        assert output[-1] == "2"
