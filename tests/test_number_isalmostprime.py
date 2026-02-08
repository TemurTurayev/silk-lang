"""
Tests for number .isAlmostPrime(k) method - has exactly k prime factors (with multiplicity).
"""

from silk.interpreter import Interpreter


class TestNumberIsAlmostPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAlmostPrime_6_2(self):
        output = self._run('print(6.isAlmostPrime(2))')
        assert output[-1] == "true"

    def test_isAlmostPrime_8_3(self):
        output = self._run('print(8.isAlmostPrime(3))')
        assert output[-1] == "true"

    def test_isAlmostPrime_6_3(self):
        output = self._run('print(6.isAlmostPrime(3))')
        assert output[-1] == "false"
