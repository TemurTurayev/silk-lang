"""
Tests for array .mapBitAlign288230376151711744() method - align up to nearest multiple of 288230376151711744.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign288230376151711744:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign288230376151711744_basic(self):
        output = self._run('print([0, 1, 144115188075855871, 144115188075855872, 288230376151711744].mapBitAlign288230376151711744())')
        assert output[-1] == '[0, 288230376151711744, 288230376151711744, 288230376151711744, 288230376151711744]'

    def test_mapBitAlign288230376151711744_exact(self):
        output = self._run('print([576460752303423488, 864691128455135232].mapBitAlign288230376151711744())')
        assert output[-1] == '[576460752303423488, 864691128455135232]'
