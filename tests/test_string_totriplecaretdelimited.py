"""
Tests for string .toTripleCaretDelimited() method - split words by ^^^.
"""

from silk.interpreter import Interpreter


class TestStringToTripleCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleCaretDelimited_basic(self):
        output = self._run('print("hello world".toTripleCaretDelimited())')
        assert output[-1] == "hello^^^world"

    def test_toTripleCaretDelimited_three(self):
        output = self._run('print("a b c".toTripleCaretDelimited())')
        assert output[-1] == "a^^^b^^^c"
