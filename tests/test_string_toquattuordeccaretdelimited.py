"""
Tests for string .toQuattuordecCaretDelimited() method - join words with 14 carets.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecCaretDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^^^^^^world"

    def test_toQuattuordecCaretDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^^^^^^b^^^^^^^^^^^^^^c"
