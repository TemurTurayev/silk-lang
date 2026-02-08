"""
Tests for array .mapTrailingZeros() method - count trailing zeros in binary.
"""

from silk.interpreter import Interpreter


class TestArrayMapTrailingZeros:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTrailingZeros_basic(self):
        output = self._run('print([8, 12, 7].mapTrailingZeros())')
        # 8=1000(3), 12=1100(2), 7=111(0)
        assert output[-1] == '[3, 2, 0]'

    def test_mapTrailingZeros_values(self):
        output = self._run('print([16, 6, 1].mapTrailingZeros())')
        # 16=10000(4), 6=110(1), 1=1(0)
        assert output[-1] == '[4, 1, 0]'
