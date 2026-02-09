"""
Tests for array .mapBitAlign134217728() method - align up to nearest multiple of 134217728.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign134217728:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign134217728_basic(self):
        output = self._run('print([0, 1, 67108863, 67108864, 134217728].mapBitAlign134217728())')
        assert output[-1] == '[0, 134217728, 134217728, 134217728, 134217728]'

    def test_mapBitAlign134217728_exact(self):
        output = self._run('print([268435456, 402653184].mapBitAlign134217728())')
        assert output[-1] == '[268435456, 402653184]'
