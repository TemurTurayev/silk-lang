"""
Tests for array .mapParityBit() method - parity bit (0=even 1s, 1=odd 1s) for each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapParityBit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapParityBit_basic(self):
        output = self._run('print([7, 8, 15].mapParityBit())')
        # 7=111(3 ones, odd=1), 8=1000(1 one, odd=1), 15=1111(4 ones, even=0)
        assert output[-1] == '[1, 1, 0]'

    def test_mapParityBit_values(self):
        output = self._run('print([0, 3, 5].mapParityBit())')
        # 0=0(0 ones, even=0), 3=11(2 ones, even=0), 5=101(2 ones, even=0)
        assert output[-1] == '[0, 0, 0]'
