"""
Tests for array .mapBitAlign35184372088832() method - align up to nearest multiple of 35184372088832.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign35184372088832:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign35184372088832_basic(self):
        output = self._run('print([0, 1, 17592186044415, 17592186044416, 35184372088832].mapBitAlign35184372088832())')
        assert output[-1] == '[0, 35184372088832, 35184372088832, 35184372088832, 35184372088832]'

    def test_mapBitAlign35184372088832_exact(self):
        output = self._run('print([70368744177664, 105553116266496].mapBitAlign35184372088832())')
        assert output[-1] == '[70368744177664, 105553116266496]'
