"""
Tests for array .mapBitAlign9007199254740992() method - align up to nearest multiple of 9007199254740992.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign9007199254740992:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign9007199254740992_basic(self):
        output = self._run('print([0, 1, 4503599627370495, 4503599627370496, 9007199254740992].mapBitAlign9007199254740992())')
        assert output[-1] == '[0, 9007199254740992, 9007199254740992, 9007199254740992, 9007199254740992]'

    def test_mapBitAlign9007199254740992_exact(self):
        output = self._run('print([18014398509481984, 27021597764222976].mapBitAlign9007199254740992())')
        assert output[-1] == '[18014398509481984, 27021597764222976]'
