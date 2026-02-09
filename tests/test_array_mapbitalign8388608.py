"""
Tests for array .mapBitAlign8388608() method - align up to nearest multiple of 8388608.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign8388608:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign8388608_basic(self):
        output = self._run('print([0, 1, 4194303, 4194304, 8388608].mapBitAlign8388608())')
        assert output[-1] == '[0, 8388608, 8388608, 8388608, 8388608]'

    def test_mapBitAlign8388608_exact(self):
        output = self._run('print([16777216, 25165824].mapBitAlign8388608())')
        assert output[-1] == '[16777216, 25165824]'
