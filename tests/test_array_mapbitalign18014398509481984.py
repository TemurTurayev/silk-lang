"""
Tests for array .mapBitAlign18014398509481984() method - align up to nearest multiple of 18014398509481984.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign18014398509481984:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign18014398509481984_basic(self):
        output = self._run('print([0, 1, 9007199254740991, 9007199254740992, 18014398509481984].mapBitAlign18014398509481984())')
        assert output[-1] == '[0, 18014398509481984, 18014398509481984, 18014398509481984, 18014398509481984]'

    def test_mapBitAlign18014398509481984_exact(self):
        output = self._run('print([36028797018963968, 54043195528445952].mapBitAlign18014398509481984())')
        assert output[-1] == '[36028797018963968, 54043195528445952]'
