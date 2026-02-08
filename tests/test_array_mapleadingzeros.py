"""
Tests for array .mapLeadingZeros() method - count leading zeros in 8-bit binary.
"""

from silk.interpreter import Interpreter


class TestArrayMapLeadingZeros:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapLeadingZeros_basic(self):
        output = self._run('print([1, 128, 255].mapLeadingZeros())')
        # 1=00000001(7), 128=10000000(0), 255=11111111(0)
        assert output[-1] == '[7, 0, 0]'

    def test_mapLeadingZeros_values(self):
        output = self._run('print([0, 64, 16].mapLeadingZeros())')
        # 0=00000000(8), 64=01000000(1), 16=00010000(3)
        assert output[-1] == '[8, 1, 3]'
