"""
Tests for array .mapBitAlign1125899906842624() method - align up to nearest multiple of 1125899906842624.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1125899906842624:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1125899906842624_basic(self):
        output = self._run('print([0, 1, 562949953421311, 562949953421312, 1125899906842624].mapBitAlign1125899906842624())')
        assert output[-1] == '[0, 1125899906842624, 1125899906842624, 1125899906842624, 1125899906842624]'

    def test_mapBitAlign1125899906842624_exact(self):
        output = self._run('print([2251799813685248, 3377699720527872].mapBitAlign1125899906842624())')
        assert output[-1] == '[2251799813685248, 3377699720527872]'
