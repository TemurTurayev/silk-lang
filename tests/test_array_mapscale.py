"""
Tests for array .mapScale() method - scale values to 0-N range.
"""

from silk.interpreter import Interpreter


class TestArrayMapScale:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapScale_basic(self):
        output = self._run('print([0, 5, 10].mapScale(100))')
        assert output[-1] == '[0, 50, 100]'

    def test_mapScale_simple(self):
        output = self._run('print([1, 2, 3].mapScale(10))')
        assert output[-1] == '[0, 5, 10]'
