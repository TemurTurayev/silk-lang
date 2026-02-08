"""
Tests for array .mapToBinary() method - convert each element to binary string.
"""

from silk.interpreter import Interpreter


class TestArrayMapToBinary:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToBinary_basic(self):
        output = self._run('print([1, 2, 3, 4].mapToBinary())')
        assert output[-1] == '[1, 10, 11, 100]'

    def test_mapToBinary_larger(self):
        output = self._run('print([8, 15, 16].mapToBinary())')
        assert output[-1] == '[1000, 1111, 10000]'
