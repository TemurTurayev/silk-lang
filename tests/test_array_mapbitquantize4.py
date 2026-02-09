"""
Tests for array .mapBitQuantize4() method - quantize to nearest multiple of 4.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize4:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize4_basic(self):
        output = self._run('print([1, 5, 8, 14].mapBitQuantize4())')
        # 1->0, 5->4, 8->8, 14->12
        assert output[-1] == '[0, 4, 8, 12]'

    def test_mapBitQuantize4_exact(self):
        output = self._run('print([0, 4, 8, 16].mapBitQuantize4())')
        assert output[-1] == '[0, 4, 8, 16]'
