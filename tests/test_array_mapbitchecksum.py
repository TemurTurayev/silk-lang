"""
Tests for array .mapBitChecksum() method - XOR all bytes together as running checksum.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitChecksum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitChecksum_basic(self):
        output = self._run('print([5, 3, 7].mapBitChecksum())')
        # running XOR: [5, 5^3=6, 5^3^7=1]
        assert output[-1] == '[5, 6, 1]'

    def test_mapBitChecksum_single(self):
        output = self._run('print([0, 255, 128].mapBitChecksum())')
        # [0, 0^255=255, 0^255^128=127]
        assert output[-1] == '[0, 255, 127]'
