"""
Tests for array .mapNormalize() method - normalize values to 0..1 range.
"""

from silk.interpreter import Interpreter


class TestArrayMapNormalize:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapNormalize_basic(self):
        output = self._run('print([0, 5, 10].mapNormalize())')
        assert output[-1] == "[0, 0.5, 1]"

    def test_mapNormalize_equal(self):
        output = self._run('print([3, 3, 3].mapNormalize())')
        assert output[-1] == "[0, 0, 0]"
