"""
Tests for array .mapSignExtend16() method - sign-extend 8-bit values to 16-bit signed.
"""

from silk.interpreter import Interpreter


class TestArrayMapSignExtend16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSignExtend16_basic(self):
        output = self._run('print([127, 128, 255].mapSignExtend16())')
        # 127->127, 128->-128, 255->-1
        assert output[-1] == '[127, -128, -1]'

    def test_mapSignExtend16_small(self):
        output = self._run('print([0, 1, 200].mapSignExtend16())')
        # 0->0, 1->1, 200->-56
        assert output[-1] == '[0, 1, -56]'
