"""
Tests for array .mapPower() method - raise each element to given power.
"""

from silk.interpreter import Interpreter


class TestArrayMapPower:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPower_basic(self):
        output = self._run('print([2, 3, 4].mapPower(3))')
        assert output[-1] == '[8, 27, 64]'

    def test_mapPower_square(self):
        output = self._run('print([1, 5, 10].mapPower(2))')
        assert output[-1] == '[1, 25, 100]'
