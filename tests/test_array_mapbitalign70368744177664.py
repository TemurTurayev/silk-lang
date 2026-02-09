"""
Tests for array .mapBitAlign70368744177664() method - align up to nearest multiple of 70368744177664.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign70368744177664:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign70368744177664_basic(self):
        output = self._run('print([0, 1, 35184372088831, 35184372088832, 70368744177664].mapBitAlign70368744177664())')
        assert output[-1] == '[0, 70368744177664, 70368744177664, 70368744177664, 70368744177664]'

    def test_mapBitAlign70368744177664_exact(self):
        output = self._run('print([140737488355328, 211106232532992].mapBitAlign70368744177664())')
        assert output[-1] == '[140737488355328, 211106232532992]'
