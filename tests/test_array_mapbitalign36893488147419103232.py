"""
Tests for array .mapBitAlign36893488147419103232() method - align up to nearest multiple of 36893488147419103232.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign36893488147419103232:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign36893488147419103232_basic(self):
        output = self._run('print([0, 1, 18446744073709551615, 18446744073709551616, 36893488147419103232].mapBitAlign36893488147419103232())')
        assert output[-1] == '[0, 36893488147419103232, 36893488147419103232, 36893488147419103232, 36893488147419103232]'

    def test_mapBitAlign36893488147419103232_exact(self):
        output = self._run('print([73786976294838206464, 110680464442257309696].mapBitAlign36893488147419103232())')
        assert output[-1] == '[73786976294838206464, 110680464442257309696]'
