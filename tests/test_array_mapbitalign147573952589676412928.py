"""
Tests for array .mapBitAlign147573952589676412928() method - align up to nearest multiple of 147573952589676412928.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign147573952589676412928:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign147573952589676412928_basic(self):
        output = self._run('print([0, 1, 73786976294838206463, 73786976294838206464, 147573952589676412928].mapBitAlign147573952589676412928())')
        assert output[-1] == '[0, 147573952589676412928, 147573952589676412928, 147573952589676412928, 147573952589676412928]'

    def test_mapBitAlign147573952589676412928_exact(self):
        output = self._run('print([295147905179352825856, 442721857769029238784].mapBitAlign147573952589676412928())')
        assert output[-1] == '[295147905179352825856, 442721857769029238784]'
