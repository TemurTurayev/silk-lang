"""
Tests for string .toTripleColonDelimited() method - split words by :::.
"""

from silk.interpreter import Interpreter


class TestStringToTripleColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleColonDelimited_basic(self):
        output = self._run('print("hello world".toTripleColonDelimited())')
        assert output[-1] == "hello:::world"

    def test_toTripleColonDelimited_three(self):
        output = self._run('print("a b c".toTripleColonDelimited())')
        assert output[-1] == "a:::b:::c"
