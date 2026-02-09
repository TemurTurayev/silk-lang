"""
Tests for array .mapBitAlign281474976710656() method - align up to nearest multiple of 281474976710656.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign281474976710656:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign281474976710656_basic(self):
        output = self._run('print([0, 1, 140737488355327, 140737488355328, 281474976710656].mapBitAlign281474976710656())')
        assert output[-1] == '[0, 281474976710656, 281474976710656, 281474976710656, 281474976710656]'

    def test_mapBitAlign281474976710656_exact(self):
        output = self._run('print([562949953421312, 844424930131968].mapBitAlign281474976710656())')
        assert output[-1] == '[562949953421312, 844424930131968]'
