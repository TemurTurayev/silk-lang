"""
Tests for array .mapBitAlign4611686018427387904() method - align up to nearest multiple of 4611686018427387904.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4611686018427387904:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4611686018427387904_basic(self):
        output = self._run('print([0, 1, 2305843009213693951, 2305843009213693952, 4611686018427387904].mapBitAlign4611686018427387904())')
        assert output[-1] == '[0, 4611686018427387904, 4611686018427387904, 4611686018427387904, 4611686018427387904]'

    def test_mapBitAlign4611686018427387904_exact(self):
        output = self._run('print([9223372036854775808, 13835058055282163712].mapBitAlign4611686018427387904())')
        assert output[-1] == '[9223372036854775808, 13835058055282163712]'
