"""
Tests for array .mapBitAlign151115727451828646838272() method - align up to nearest multiple of 151115727451828646838272.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign151115727451828646838272:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign151115727451828646838272_basic(self):
        output = self._run('print([0, 1, 75557863725914323419135, 75557863725914323419136, 151115727451828646838272].mapBitAlign151115727451828646838272())')
        assert output[-1] == '[0, 151115727451828646838272, 151115727451828646838272, 151115727451828646838272, 151115727451828646838272]'

    def test_mapBitAlign151115727451828646838272_exact(self):
        output = self._run('print([302231454903657293676544, 453347182355485940514816].mapBitAlign151115727451828646838272())')
        assert output[-1] == '[302231454903657293676544, 453347182355485940514816]'
