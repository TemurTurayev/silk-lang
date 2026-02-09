"""
Tests for string .toQuindecCaretDelimited() method - join words with 15 carets.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecCaretDelimited_basic(self):
        output = self._run('print("hello world".toQuindecCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^^^^^^^world"

    def test_toQuindecCaretDelimited_three(self):
        output = self._run('print("a b c".toQuindecCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^^^^^^^b^^^^^^^^^^^^^^^c"
