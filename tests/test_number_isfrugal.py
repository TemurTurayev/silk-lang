"""
Tests for number .isFrugal() method - prime factorization uses fewer digits than n.
"""

from silk.interpreter import Interpreter


class TestNumberIsFrugal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isFrugal_125(self):
        output = self._run('print(125.isFrugal())')
        assert output[-1] == "true"

    def test_isFrugal_4(self):
        output = self._run('print(4.isFrugal())')
        assert output[-1] == "false"
