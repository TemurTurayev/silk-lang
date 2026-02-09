"""
Tests for array .mapBitAlign604462909807314587353088() method - align up to nearest multiple of 604462909807314587353088.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign604462909807314587353088:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign604462909807314587353088_basic(self):
        output = self._run('print([0, 1, 302231454903657293676543, 302231454903657293676544, 604462909807314587353088].mapBitAlign604462909807314587353088())')
        assert output[-1] == '[0, 604462909807314587353088, 604462909807314587353088, 604462909807314587353088, 604462909807314587353088]'

    def test_mapBitAlign604462909807314587353088_exact(self):
        output = self._run('print([1208925819614629174706176, 1813388729421943762059264].mapBitAlign604462909807314587353088())')
        assert output[-1] == '[1208925819614629174706176, 1813388729421943762059264]'
