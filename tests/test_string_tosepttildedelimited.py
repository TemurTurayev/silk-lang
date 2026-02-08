"""
Tests for string .toSeptTildeDelimited() method - split words by ~~~~~~~.
"""

from silk.interpreter import Interpreter


class TestStringToSeptTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptTildeDelimited_basic(self):
        output = self._run('print("hello world".toSeptTildeDelimited())')
        assert output[-1] == "hello~~~~~~~world"

    def test_toSeptTildeDelimited_three(self):
        output = self._run('print("a b c".toSeptTildeDelimited())')
        assert output[-1] == "a~~~~~~~b~~~~~~~c"
