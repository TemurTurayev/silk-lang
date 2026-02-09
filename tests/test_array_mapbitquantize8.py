"""
Tests for array .mapBitQuantize8() method - quantize to nearest multiple of 8.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize8_basic(self):
        output = self._run('print([3, 9, 16, 23].mapBitQuantize8())')
        # 3->0, 9->8, 16->16, 23->16
        assert output[-1] == '[0, 8, 16, 16]'

    def test_mapBitQuantize8_exact(self):
        output = self._run('print([0, 8, 16, 24].mapBitQuantize8())')
        assert output[-1] == '[0, 8, 16, 24]'
