"""
Tests for array .mapGrayCode() method - convert each element to Gray code.
"""

from silk.interpreter import Interpreter


class TestArrayMapGrayCode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapGrayCode_basic(self):
        output = self._run('print([0, 1, 2, 3].mapGrayCode())')
        # 0^0=0, 1^0=1, 2^1=3, 3^1=2
        assert output[-1] == '[0, 1, 3, 2]'

    def test_mapGrayCode_larger(self):
        output = self._run('print([4, 5, 6, 7].mapGrayCode())')
        # 4^2=6, 5^2=7, 6^3=5, 7^3=4
        assert output[-1] == '[6, 7, 5, 4]'
