"""
Tests for array .mapPow10() method - raise 10 to the power of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapPow10:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPow10_basic(self):
        output = self._run('print([0, 1, 2, 3].mapPow10())')
        assert output[-1] == '[1, 10, 100, 1000]'

    def test_mapPow10_larger(self):
        output = self._run('print([4, 5].mapPow10())')
        assert output[-1] == '[10000, 100000]'
