"""
Tests for array .mapToHexString() method - convert each element to hex with 0x prefix.
"""

from silk.interpreter import Interpreter


class TestArrayMapToHexString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToHexString_basic(self):
        output = self._run('print([10, 255].mapToHexString())')
        assert output[-1] == '[0xa, 0xff]'

    def test_mapToHexString_small(self):
        output = self._run('print([0, 1, 16].mapToHexString())')
        assert output[-1] == '[0x0, 0x1, 0x10]'
