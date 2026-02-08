"""
Tests for array .mapBitLength() method - number of bits needed to represent each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitLength:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitLength_basic(self):
        output = self._run('print([1, 2, 4, 7, 8].mapBitLength())')
        # 1->1, 10->2, 100->3, 111->3, 1000->4
        assert output[-1] == "[1, 2, 3, 3, 4]"

    def test_mapBitLength_powers(self):
        output = self._run('print([16, 31, 32].mapBitLength())')
        # 10000->5, 11111->5, 100000->6
        assert output[-1] == "[5, 5, 6]"
