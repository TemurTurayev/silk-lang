"""
Tests for array .mapBitAlign17592186044416() method - align up to nearest multiple of 17592186044416.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign17592186044416:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign17592186044416_basic(self):
        output = self._run('print([0, 1, 8796093022207, 8796093022208, 17592186044416].mapBitAlign17592186044416())')
        assert output[-1] == '[0, 17592186044416, 17592186044416, 17592186044416, 17592186044416]'

    def test_mapBitAlign17592186044416_exact(self):
        output = self._run('print([35184372088832, 52776558133248].mapBitAlign17592186044416())')
        assert output[-1] == '[35184372088832, 52776558133248]'
