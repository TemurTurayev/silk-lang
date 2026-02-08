"""
Tests for string .toTripleTildeDelimited() method - split words by ~~~.
"""

from silk.interpreter import Interpreter


class TestStringToTripleTildeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleTildeDelimited_basic(self):
        output = self._run('print("hello world".toTripleTildeDelimited())')
        assert output[-1] == "hello~~~world"

    def test_toTripleTildeDelimited_three(self):
        output = self._run('print("a b c".toTripleTildeDelimited())')
        assert output[-1] == "a~~~b~~~c"
