"""
Tests for array .mapClamp() method - clamp each element between min and max.
"""

from silk.interpreter import Interpreter


class TestArrayMapClamp:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapClamp_basic(self):
        output = self._run('print([1, 5, 10, 15, 20].mapClamp(5, 15))')
        assert output[-1] == '[5, 5, 10, 15, 15]'

    def test_mapClamp_all_in_range(self):
        output = self._run('print([3, 4, 5].mapClamp(1, 10))')
        assert output[-1] == '[3, 4, 5]'
