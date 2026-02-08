"""
Tests for string .toTripleHashDelimited() method - split words by ###.
"""

from silk.interpreter import Interpreter


class TestStringToTripleHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleHashDelimited_basic(self):
        output = self._run('print("hello world".toTripleHashDelimited())')
        assert output[-1] == "hello###world"

    def test_toTripleHashDelimited_three(self):
        output = self._run('print("a b c".toTripleHashDelimited())')
        assert output[-1] == "a###b###c"
