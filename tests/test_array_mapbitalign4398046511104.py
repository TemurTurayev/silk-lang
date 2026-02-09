"""
Tests for array .mapBitAlign4398046511104() method - align up to nearest multiple of 4398046511104.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4398046511104:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4398046511104_basic(self):
        output = self._run('print([0, 1, 2199023255551, 2199023255552, 4398046511104].mapBitAlign4398046511104())')
        assert output[-1] == '[0, 4398046511104, 4398046511104, 4398046511104, 4398046511104]'

    def test_mapBitAlign4398046511104_exact(self):
        output = self._run('print([8796093022208, 13194139533312].mapBitAlign4398046511104())')
        assert output[-1] == '[8796093022208, 13194139533312]'
