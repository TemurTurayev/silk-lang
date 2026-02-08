"""
Tests for array .mapBitNextPowerOf2() method - smallest power of 2 >= each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitNextPowerOf2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitNextPowerOf2_basic(self):
        output = self._run('print([3, 5, 7, 9].mapBitNextPowerOf2())')
        # 3->4; 5->8; 7->8; 9->16
        assert output[-1] == '[4, 8, 8, 16]'

    def test_mapBitNextPowerOf2_exact(self):
        output = self._run('print([1, 2, 4, 8, 16].mapBitNextPowerOf2())')
        # already powers of 2 -> same values
        assert output[-1] == '[1, 2, 4, 8, 16]'
