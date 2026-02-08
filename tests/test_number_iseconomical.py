"""
Tests for number .isEconomical() method - alias for isFrugal.
"""

from silk.interpreter import Interpreter


class TestNumberIsEconomical:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEconomical_125(self):
        output = self._run('print(125.isEconomical())')
        assert output[-1] == "true"

    def test_isEconomical_4(self):
        output = self._run('print(4.isEconomical())')
        assert output[-1] == "false"
