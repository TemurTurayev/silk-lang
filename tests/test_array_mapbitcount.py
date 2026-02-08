"""
Tests for array .mapBitCount() method - count of set bits (1s) in binary representation.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitCount_basic(self):
        output = self._run('print([1, 2, 3, 7, 8].mapBitCount())')
        # 1->1, 10->1, 11->2, 111->3, 1000->1
        assert output[-1] == "[1, 1, 2, 3, 1]"

    def test_mapBitCount_powers(self):
        output = self._run('print([4, 15, 16].mapBitCount())')
        # 100->1, 1111->4, 10000->1
        assert output[-1] == "[1, 4, 1]"
