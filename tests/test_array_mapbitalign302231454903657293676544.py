"""
Tests for array .mapBitAlign302231454903657293676544() method - align up to nearest multiple of 302231454903657293676544.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign302231454903657293676544:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign302231454903657293676544_basic(self):
        output = self._run('print([0, 1, 151115727451828646838271, 151115727451828646838272, 302231454903657293676544].mapBitAlign302231454903657293676544())')
        assert output[-1] == '[0, 302231454903657293676544, 302231454903657293676544, 302231454903657293676544, 302231454903657293676544]'

    def test_mapBitAlign302231454903657293676544_exact(self):
        output = self._run('print([604462909807314587353088, 906694364710971881029632].mapBitAlign302231454903657293676544())')
        assert output[-1] == '[604462909807314587353088, 906694364710971881029632]'
