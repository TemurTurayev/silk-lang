"""
Tests for number .divisorCount() method.
"""

from silk.interpreter import Interpreter


class TestNumberDivisorCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_divisorCount_basic(self):
        output = self._run('print(12.divisorCount())')
        assert output[-1] == "6"

    def test_divisorCount_prime(self):
        output = self._run('print(7.divisorCount())')
        assert output[-1] == "2"
