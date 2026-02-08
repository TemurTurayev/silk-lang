"""
Tests for array .mapBitAlternating() method - check if bits alternate (01 or 10 pattern).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlternating:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlternating_basic(self):
        output = self._run('print([5, 10, 7].mapBitAlternating())')
        # 5=101 alternating=true, 10=1010 alternating=true, 7=111 alternating=false
        assert output[-1] == '[true, true, false]'

    def test_mapBitAlternating_single(self):
        output = self._run('print([0, 1, 2, 3].mapBitAlternating())')
        # 0=0 true, 1=1 true, 2=10 true, 3=11 false
        assert output[-1] == '[true, true, true, false]'
