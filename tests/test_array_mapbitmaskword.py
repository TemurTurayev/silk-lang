"""
Tests for array .mapBitMaskWord() method - keep only the lowest word (16 bits).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskWord:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskWord_basic(self):
        output = self._run('print([65536, 65535, 70000].mapBitMaskWord())')
        # 65536 & 0xFFFF = 0; 65535 & 0xFFFF = 65535; 70000 & 0xFFFF = 4464
        assert output[-1] == '[0, 65535, 4464]'

    def test_mapBitMaskWord_small(self):
        output = self._run('print([0, 255, 1000].mapBitMaskWord())')
        # all < 65536, so unchanged
        assert output[-1] == '[0, 255, 1000]'
