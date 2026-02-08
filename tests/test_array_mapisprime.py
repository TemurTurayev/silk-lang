"""
Tests for array .mapIsPrime() method - check if each element is prime.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsPrime_mixed(self):
        output = self._run('print([1, 2, 3, 4, 5].mapIsPrime())')
        assert output[-1] == "[false, true, true, false, true]"

    def test_mapIsPrime_allPrime(self):
        output = self._run('print([2, 3, 5, 7].mapIsPrime())')
        assert output[-1] == "[true, true, true, true]"
