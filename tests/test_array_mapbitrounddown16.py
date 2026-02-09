"""
Tests for array .mapBitRoundDown16() method - round down to nearest multiple of 16.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown16_basic(self):
        output = self._run('print([15, 16, 17, 31].mapBitRoundDown16())')
        # 15->0, 16->16, 17->16, 31->16
        assert output[-1] == '[0, 16, 16, 16]'

    def test_mapBitRoundDown16_exact(self):
        output = self._run('print([0, 32, 48, 64].mapBitRoundDown16())')
        assert output[-1] == '[0, 32, 48, 64]'
