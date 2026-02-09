"""
Tests for array .mapBitAlign75557863725914323419136() method - align up to nearest multiple of 75557863725914323419136.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign75557863725914323419136:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign75557863725914323419136_basic(self):
        output = self._run('print([0, 1, 37778931862957161709567, 37778931862957161709568, 75557863725914323419136].mapBitAlign75557863725914323419136())')
        assert output[-1] == '[0, 75557863725914323419136, 75557863725914323419136, 75557863725914323419136, 75557863725914323419136]'

    def test_mapBitAlign75557863725914323419136_exact(self):
        output = self._run('print([151115727451828646838272, 226673591177742970257408].mapBitAlign75557863725914323419136())')
        assert output[-1] == '[151115727451828646838272, 226673591177742970257408]'
