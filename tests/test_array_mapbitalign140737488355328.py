"""
Tests for array .mapBitAlign140737488355328() method - align up to nearest multiple of 140737488355328.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign140737488355328:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign140737488355328_basic(self):
        output = self._run('print([0, 1, 70368744177663, 70368744177664, 140737488355328].mapBitAlign140737488355328())')
        assert output[-1] == '[0, 140737488355328, 140737488355328, 140737488355328, 140737488355328]'

    def test_mapBitAlign140737488355328_exact(self):
        output = self._run('print([281474976710656, 422212465065984].mapBitAlign140737488355328())')
        assert output[-1] == '[281474976710656, 422212465065984]'
