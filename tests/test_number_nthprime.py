"""
Tests for number .nthPrime() method.
"""

from silk.interpreter import Interpreter


class TestNumberNthPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_nthPrime_1(self):
        output = self._run('print(1.nthPrime())')
        assert output[-1] == "2"

    def test_nthPrime_5(self):
        output = self._run('print(5.nthPrime())')
        assert output[-1] == "11"

    def test_nthPrime_10(self):
        output = self._run('print(10.nthPrime())')
        assert output[-1] == "29"
