"""
Tests for array .mapBitAlign73786976294838206464() method - align up to nearest multiple of 73786976294838206464.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign73786976294838206464:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign73786976294838206464_basic(self):
        output = self._run('print([0, 1, 36893488147419103231, 36893488147419103232, 73786976294838206464].mapBitAlign73786976294838206464())')
        assert output[-1] == '[0, 73786976294838206464, 73786976294838206464, 73786976294838206464, 73786976294838206464]'

    def test_mapBitAlign73786976294838206464_exact(self):
        output = self._run('print([147573952589676412928, 221360928884514619392].mapBitAlign73786976294838206464())')
        assert output[-1] == '[147573952589676412928, 221360928884514619392]'
