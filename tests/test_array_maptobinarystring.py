"""
Tests for array .mapToBinaryString() method - convert each element to binary with 0b prefix.
"""

from silk.interpreter import Interpreter


class TestArrayMapToBinaryString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToBinaryString_basic(self):
        output = self._run('print([5, 10].mapToBinaryString())')
        assert output[-1] == '[0b101, 0b1010]'

    def test_mapToBinaryString_small(self):
        output = self._run('print([0, 1, 2].mapToBinaryString())')
        assert output[-1] == '[0b0, 0b1, 0b10]'
