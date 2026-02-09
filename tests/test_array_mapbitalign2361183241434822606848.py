"""
Tests for array .mapBitAlign2361183241434822606848() method - align up to nearest multiple of 2361183241434822606848.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign2361183241434822606848:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign2361183241434822606848_basic(self):
        output = self._run('print([0, 1, 1180591620717411303423, 1180591620717411303424, 2361183241434822606848].mapBitAlign2361183241434822606848())')
        assert output[-1] == '[0, 2361183241434822606848, 2361183241434822606848, 2361183241434822606848, 2361183241434822606848]'

    def test_mapBitAlign2361183241434822606848_exact(self):
        output = self._run('print([4722366482869645213696, 7083549724304467820544].mapBitAlign2361183241434822606848())')
        assert output[-1] == '[4722366482869645213696, 7083549724304467820544]'
