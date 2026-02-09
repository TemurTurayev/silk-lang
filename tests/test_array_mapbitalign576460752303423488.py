"""
Tests for array .mapBitAlign576460752303423488() method - align up to nearest multiple of 576460752303423488.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign576460752303423488:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign576460752303423488_basic(self):
        output = self._run('print([0, 1, 288230376151711743, 288230376151711744, 576460752303423488].mapBitAlign576460752303423488())')
        assert output[-1] == '[0, 576460752303423488, 576460752303423488, 576460752303423488, 576460752303423488]'

    def test_mapBitAlign576460752303423488_exact(self):
        output = self._run('print([1152921504606846976, 1729382256910270464].mapBitAlign576460752303423488())')
        assert output[-1] == '[1152921504606846976, 1729382256910270464]'
