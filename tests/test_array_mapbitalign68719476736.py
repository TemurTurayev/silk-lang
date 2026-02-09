"""
Tests for array .mapBitAlign68719476736() method - align up to nearest multiple of 68719476736.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign68719476736:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign68719476736_basic(self):
        output = self._run('print([0, 1, 34359738367, 34359738368, 68719476736].mapBitAlign68719476736())')
        assert output[-1] == '[0, 68719476736, 68719476736, 68719476736, 68719476736]'

    def test_mapBitAlign68719476736_exact(self):
        output = self._run('print([137438953472, 206158430208].mapBitAlign68719476736())')
        assert output[-1] == '[137438953472, 206158430208]'
