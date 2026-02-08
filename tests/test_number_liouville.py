"""
Tests for number .liouville() method - Liouville function.
lambda(n) = (-1)^Omega(n) where Omega(n) is number of prime factors with multiplicity.
"""

from silk.interpreter import Interpreter


class TestNumberLiouville:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_liouville_6(self):
        output = self._run('print(6.liouville())')
        assert output[-1] == "1"

    def test_liouville_2(self):
        output = self._run('print(2.liouville())')
        assert output[-1] == "-1"
