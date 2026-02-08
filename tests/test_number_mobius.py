"""
Tests for number .mobius() method - Mobius function.
mu(n) = 1 if n is square-free with even number of prime factors
mu(n) = -1 if n is square-free with odd number of prime factors
mu(n) = 0 if n has a squared prime factor
"""

from silk.interpreter import Interpreter


class TestNumberMobius:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mobius_6(self):
        output = self._run('print(6.mobius())')
        assert output[-1] == "1"

    def test_mobius_4(self):
        output = self._run('print(4.mobius())')
        assert output[-1] == "0"
