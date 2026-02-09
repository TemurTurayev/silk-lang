"""
Tests for array .mapBitAlign2251799813685248() method - align up to nearest multiple of 2251799813685248.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign2251799813685248:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign2251799813685248_basic(self):
        output = self._run('print([0, 1, 1125899906842623, 1125899906842624, 2251799813685248].mapBitAlign2251799813685248())')
        assert output[-1] == '[0, 2251799813685248, 2251799813685248, 2251799813685248, 2251799813685248]'

    def test_mapBitAlign2251799813685248_exact(self):
        output = self._run('print([4503599627370496, 6755399441055744].mapBitAlign2251799813685248())')
        assert output[-1] == '[4503599627370496, 6755399441055744]'
