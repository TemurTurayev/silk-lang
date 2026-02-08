"""
Tests for array .mapPopCount() method - count set bits in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapPopCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPopCount_basic(self):
        output = self._run('print([7, 8, 15].mapPopCount())')
        # 7=111(3 bits), 8=1000(1 bit), 15=1111(4 bits)
        assert output[-1] == '[3, 1, 4]'

    def test_mapPopCount_zeros(self):
        output = self._run('print([0, 1, 255].mapPopCount())')
        assert output[-1] == '[0, 1, 8]'
