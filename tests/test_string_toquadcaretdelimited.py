"""
Tests for string .toQuadCaretDelimited() method - split words by ^^^^.
"""

from silk.interpreter import Interpreter


class TestStringToQuadCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadCaretDelimited_basic(self):
        output = self._run('print("hello world".toQuadCaretDelimited())')
        assert output[-1] == "hello^^^^world"

    def test_toQuadCaretDelimited_three(self):
        output = self._run('print("a b c".toQuadCaretDelimited())')
        assert output[-1] == "a^^^^b^^^^c"
