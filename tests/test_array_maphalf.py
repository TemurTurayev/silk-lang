"""
Tests for array .mapHalf() method - halve each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapHalf:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapHalf_basic(self):
        output = self._run('print([2, 4, 6].mapHalf())')
        assert output[-1] == "[1, 2, 3]"

    def test_mapHalf_odd(self):
        output = self._run('print([1, 3, 5].mapHalf())')
        assert output[-1] == "[0.5, 1.5, 2.5]"
