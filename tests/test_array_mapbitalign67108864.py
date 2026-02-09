"""
Tests for array .mapBitAlign67108864() method - align up to nearest multiple of 67108864.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign67108864:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign67108864_basic(self):
        output = self._run('print([0, 1, 33554431, 33554432, 67108864].mapBitAlign67108864())')
        assert output[-1] == '[0, 67108864, 67108864, 67108864, 67108864]'

    def test_mapBitAlign67108864_exact(self):
        output = self._run('print([134217728, 201326592].mapBitAlign67108864())')
        assert output[-1] == '[134217728, 201326592]'
