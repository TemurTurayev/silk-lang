"""
Tests for array .mapBitEntropy() method - Shannon entropy of bit pattern.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitEntropy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitEntropy_basic(self):
        output = self._run('print([255, 0, 170].mapBitEntropy())')
        # 255=11111111: all 1s -> entropy 0; 0: entropy 0; 170=10101010: 4 ones 4 zeros -> entropy 1.0
        assert '0' in output[-1]

    def test_mapBitEntropy_single(self):
        output = self._run('print([1, 7].mapBitEntropy())')
        # 1=1: all 1s -> 0; 7=111: all 1s -> 0
        assert output[-1] == '[0, 0]'
