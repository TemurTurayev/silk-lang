"""
Tests for number .isCircularPrime() method - all rotations are prime.
"""

from silk.interpreter import Interpreter


class TestNumberIsCircularPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCircularPrime_197(self):
        output = self._run('print(197.isCircularPrime())')
        assert output[-1] == "true"

    def test_isCircularPrime_11(self):
        output = self._run('print(11.isCircularPrime())')
        assert output[-1] == "true"

    def test_isCircularPrime_19(self):
        output = self._run('print(19.isCircularPrime())')
        assert output[-1] == "false"
