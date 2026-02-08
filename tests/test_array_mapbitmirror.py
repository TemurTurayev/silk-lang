"""
Tests for array .mapBitMirror() method - mirror the bits (append reversed bits).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMirror:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMirror_basic(self):
        output = self._run('print([5, 3, 6].mapBitMirror())')
        # 5=101 -> 101_101 = 101101 = 45, 3=11 -> 11_11 = 1111 = 15, 6=110 -> 110_011 = 110011 = 51
        assert output[-1] == '[45, 15, 51]'

    def test_mapBitMirror_single(self):
        output = self._run('print([0, 1, 7].mapBitMirror())')
        # 0 -> 0, 1=1 -> 1_1 = 11 = 3, 7=111 -> 111_111 = 111111 = 63
        assert output[-1] == '[0, 3, 63]'
