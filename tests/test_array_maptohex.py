"""
Tests for array .mapToHex() method - convert each element to hexadecimal string.
"""

from silk.interpreter import Interpreter


class TestArrayMapToHex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToHex_basic(self):
        output = self._run('print([10, 15, 16, 255].mapToHex())')
        assert output[-1] == '[a, f, 10, ff]'

    def test_mapToHex_small(self):
        output = self._run('print([1, 9, 11].mapToHex())')
        assert output[-1] == '[1, 9, b]'
