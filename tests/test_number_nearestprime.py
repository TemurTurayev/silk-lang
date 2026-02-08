"""
Tests for number .nearestPrime() method - find closest prime number.
"""

from silk.interpreter import Interpreter


class TestNumberNearestPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_nearestPrime_prime(self):
        output = self._run('print(7.nearestPrime())')
        assert output[-1] == "7"

    def test_nearestPrime_composite(self):
        output = self._run('print(10.nearestPrime())')
        assert output[-1] == "11"

    def test_nearestPrime_4(self):
        output = self._run('print(4.nearestPrime())')
        assert output[-1] == "3"
