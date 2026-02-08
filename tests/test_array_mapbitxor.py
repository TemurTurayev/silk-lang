"""
Tests for array .mapBitXor() method - bitwise XOR each element with argument.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitXor:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitXor_basic(self):
        output = self._run('print([15, 7, 12].mapBitXor(5))')
        assert output[-1] == '[10, 2, 9]'

    def test_mapBitXor_toggle(self):
        output = self._run('print([255, 0, 128].mapBitXor(255))')
        assert output[-1] == '[0, 255, 127]'
