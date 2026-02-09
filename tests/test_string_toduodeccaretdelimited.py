"""
Tests for string .toDuodecCaretDelimited() method - split words by ^^^^^^^^^^^^ (12 carets).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecCaretDelimited_basic(self):
        output = self._run('print("hello world".toDuodecCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^^^^world"

    def test_toDuodecCaretDelimited_three(self):
        output = self._run('print("a b c".toDuodecCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^^^^b^^^^^^^^^^^^c"
