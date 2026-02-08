"""
Tests for array .mapBitPrevPowerOf2() method - largest power of 2 <= each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitPrevPowerOf2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitPrevPowerOf2_basic(self):
        output = self._run('print([3, 5, 7, 9].mapBitPrevPowerOf2())')
        # 3->2; 5->4; 7->4; 9->8
        assert output[-1] == '[2, 4, 4, 8]'

    def test_mapBitPrevPowerOf2_exact(self):
        output = self._run('print([1, 2, 4, 8, 16].mapBitPrevPowerOf2())')
        # already powers of 2 -> same values
        assert output[-1] == '[1, 2, 4, 8, 16]'
