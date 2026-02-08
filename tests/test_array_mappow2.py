"""
Tests for array .mapPow2() method - raise 2 to the power of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapPow2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPow2_basic(self):
        output = self._run('print([0, 1, 2, 3].mapPow2())')
        assert output[-1] == '[1, 2, 4, 8]'

    def test_mapPow2_larger(self):
        output = self._run('print([4, 8, 10].mapPow2())')
        assert output[-1] == '[16, 256, 1024]'
