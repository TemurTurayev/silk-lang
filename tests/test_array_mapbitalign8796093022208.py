"""
Tests for array .mapBitAlign8796093022208() method - align up to nearest multiple of 8796093022208.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign8796093022208:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign8796093022208_basic(self):
        output = self._run('print([0, 1, 4398046511103, 4398046511104, 8796093022208].mapBitAlign8796093022208())')
        assert output[-1] == '[0, 8796093022208, 8796093022208, 8796093022208, 8796093022208]'

    def test_mapBitAlign8796093022208_exact(self):
        output = self._run('print([17592186044416, 26388279066624].mapBitAlign8796093022208())')
        assert output[-1] == '[17592186044416, 26388279066624]'
