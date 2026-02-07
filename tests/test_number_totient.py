"""
Tests for number .totient() method (Euler's totient).
"""

from silk.interpreter import Interpreter


class TestNumberTotient:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_totient_basic(self):
        output = self._run('print(10.totient())')
        assert output[-1] == "4"

    def test_totient_prime(self):
        output = self._run('print(7.totient())')
        assert output[-1] == "6"
