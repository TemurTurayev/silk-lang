"""
Tests for array .mapBitAlign34359738368() method - align up to nearest multiple of 34359738368.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign34359738368:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign34359738368_basic(self):
        output = self._run('print([0, 1, 17179869183, 17179869184, 34359738368].mapBitAlign34359738368())')
        assert output[-1] == '[0, 34359738368, 34359738368, 34359738368, 34359738368]'

    def test_mapBitAlign34359738368_exact(self):
        output = self._run('print([68719476736, 103079215104].mapBitAlign34359738368())')
        assert output[-1] == '[68719476736, 103079215104]'
