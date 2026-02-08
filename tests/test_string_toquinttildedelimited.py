"""
Tests for string .toQuintTildeDelimited() method - split words by ~~~~~.
"""

from silk.interpreter import Interpreter


class TestStringToQuintTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintTildeDelimited_basic(self):
        output = self._run('print("hello world".toQuintTildeDelimited())')
        assert output[-1] == "hello~~~~~world"

    def test_toQuintTildeDelimited_three(self):
        output = self._run('print("a b c".toQuintTildeDelimited())')
        assert output[-1] == "a~~~~~b~~~~~c"
