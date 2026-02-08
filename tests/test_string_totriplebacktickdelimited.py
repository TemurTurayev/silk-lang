"""
Tests for string .toTripleBacktickDelimited() method - split words by ```.
"""

from silk.interpreter import Interpreter


class TestStringToTripleBacktickDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleBacktickDelimited_basic(self):
        output = self._run('print("hello world".toTripleBacktickDelimited())')
        assert output[-1] == "hello```world"

    def test_toTripleBacktickDelimited_three(self):
        output = self._run('print("a b c".toTripleBacktickDelimited())')
        assert output[-1] == "a```b```c"
