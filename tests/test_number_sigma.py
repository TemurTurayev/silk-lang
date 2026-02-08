"""
Tests for number .sigma() method - sum of all divisors.
"""

from silk.interpreter import Interpreter


class TestNumberSigma:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sigma_12(self):
        output = self._run('print(12.sigma())')
        assert output[-1] == "28"

    def test_sigma_6(self):
        output = self._run('print(6.sigma())')
        assert output[-1] == "12"
