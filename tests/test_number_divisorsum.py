"""
Tests for number .divisorSum() method - sum of all proper divisors including itself.
"""

from silk.interpreter import Interpreter


class TestNumberDivisorSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_divisorSum_12(self):
        output = self._run('print(12.divisorSum())')
        assert output[-1] == "28"

    def test_divisorSum_6(self):
        output = self._run('print(6.divisorSum())')
        assert output[-1] == "12"
