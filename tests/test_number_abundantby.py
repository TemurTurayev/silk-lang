"""
Tests for number .abundantBy() method - excess of aliquot sum.
"""

from silk.interpreter import Interpreter


class TestNumberAbundantBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_abundantBy_12(self):
        output = self._run('print(12.abundantBy())')
        assert output[-1] == "4"

    def test_abundantBy_6(self):
        output = self._run('print(6.abundantBy())')
        assert output[-1] == "0"

    def test_abundantBy_10(self):
        output = self._run('print(10.abundantBy())')
        assert output[-1] == "-2"
