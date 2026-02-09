"""
Tests for array .mapBitAlign137438953472() method - align up to nearest multiple of 137438953472.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign137438953472:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign137438953472_basic(self):
        output = self._run('print([0, 1, 68719476735, 68719476736, 137438953472].mapBitAlign137438953472())')
        assert output[-1] == '[0, 137438953472, 137438953472, 137438953472, 137438953472]'

    def test_mapBitAlign137438953472_exact(self):
        output = self._run('print([274877906944, 412316860416].mapBitAlign137438953472())')
        assert output[-1] == '[274877906944, 412316860416]'
