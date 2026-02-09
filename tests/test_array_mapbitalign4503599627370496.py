"""
Tests for array .mapBitAlign4503599627370496() method - align up to nearest multiple of 4503599627370496.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4503599627370496:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4503599627370496_basic(self):
        output = self._run('print([0, 1, 2251799813685247, 2251799813685248, 4503599627370496].mapBitAlign4503599627370496())')
        assert output[-1] == '[0, 4503599627370496, 4503599627370496, 4503599627370496, 4503599627370496]'

    def test_mapBitAlign4503599627370496_exact(self):
        output = self._run('print([9007199254740992, 13510798882111488].mapBitAlign4503599627370496())')
        assert output[-1] == '[9007199254740992, 13510798882111488]'
