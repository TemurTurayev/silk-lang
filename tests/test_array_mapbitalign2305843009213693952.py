"""
Tests for array .mapBitAlign2305843009213693952() method - align up to nearest multiple of 2305843009213693952.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign2305843009213693952:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign2305843009213693952_basic(self):
        output = self._run('print([0, 1, 1152921504606846975, 1152921504606846976, 2305843009213693952].mapBitAlign2305843009213693952())')
        assert output[-1] == '[0, 2305843009213693952, 2305843009213693952, 2305843009213693952, 2305843009213693952]'

    def test_mapBitAlign2305843009213693952_exact(self):
        output = self._run('print([4611686018427387904, 6917529027641081856].mapBitAlign2305843009213693952())')
        assert output[-1] == '[4611686018427387904, 6917529027641081856]'
