"""
Tests for array .mapBitAlign16777216() method - align up to nearest multiple of 16777216.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign16777216:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign16777216_basic(self):
        output = self._run('print([0, 1, 8388607, 8388608, 16777216].mapBitAlign16777216())')
        assert output[-1] == '[0, 16777216, 16777216, 16777216, 16777216]'

    def test_mapBitAlign16777216_exact(self):
        output = self._run('print([33554432, 50331648].mapBitAlign16777216())')
        assert output[-1] == '[33554432, 50331648]'
