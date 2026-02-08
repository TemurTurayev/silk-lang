"""
Tests for string .toQuadTildeDelimited() method - split words by ~~~~.
"""

from silk.interpreter import Interpreter


class TestStringToQuadTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadTildeDelimited_basic(self):
        output = self._run('print("hello world".toQuadTildeDelimited())')
        assert output[-1] == "hello~~~~world"

    def test_toQuadTildeDelimited_three(self):
        output = self._run('print("a b c".toQuadTildeDelimited())')
        assert output[-1] == "a~~~~b~~~~c"
