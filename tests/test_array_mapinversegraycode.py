"""
Tests for array .mapInverseGrayCode() method - convert Gray code back to binary.
"""

from silk.interpreter import Interpreter


class TestArrayMapInverseGrayCode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapInverseGrayCode_basic(self):
        output = self._run('print([0, 1, 3, 2].mapInverseGrayCode())')
        assert output[-1] == '[0, 1, 2, 3]'

    def test_mapInverseGrayCode_larger(self):
        output = self._run('print([6, 7, 5, 4].mapInverseGrayCode())')
        assert output[-1] == '[4, 5, 6, 7]'
