"""
Tests for string .toTildeDelimited() method - split words by tilde.
"""

from silk.interpreter import Interpreter


class TestStringToTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTildeDelimited_basic(self):
        output = self._run('print("hello world".toTildeDelimited())')
        assert output[-1] == "hello~world"

    def test_toTildeDelimited_three(self):
        output = self._run('print("a b c".toTildeDelimited())')
        assert output[-1] == "a~b~c"
