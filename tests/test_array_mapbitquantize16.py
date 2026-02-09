"""
Tests for array .mapBitQuantize16() method - quantize to nearest multiple of 16.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize16_basic(self):
        output = self._run('print([5, 17, 32, 47].mapBitQuantize16())')
        # 5->0, 17->16, 32->32, 47->32
        assert output[-1] == '[0, 16, 32, 32]'

    def test_mapBitQuantize16_exact(self):
        output = self._run('print([0, 16, 32, 48].mapBitQuantize16())')
        assert output[-1] == '[0, 16, 32, 48]'
