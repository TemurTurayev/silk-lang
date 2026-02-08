"""
Tests for array .mapBitSpread() method - spread each bit apart (insert 0 between each bit).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSpread:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSpread_basic(self):
        output = self._run('print([5, 3, 7].mapBitSpread())')
        # 5=101 -> 1_0_1 -> 010001 = 17, 3=11 -> 1_1 -> 0101 = 5, 7=111 -> 1_1_1 -> 010101 = 21
        assert output[-1] == '[17, 5, 21]'

    def test_mapBitSpread_single(self):
        output = self._run('print([0, 1, 15].mapBitSpread())')
        # 0->0, 1=1->01=1, 15=1111->01010101=85
        assert output[-1] == '[0, 1, 85]'
