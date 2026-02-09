"""
Tests for string .toVigintiCaretDelimited() method - join words with 20 carets.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiCaretDelimited_basic(self):
        output = self._run('print("hello world".toVigintiCaretDelimited())')
        assert output[-1] == "hello" + "^" * 20 + "world"

    def test_toVigintiCaretDelimited_multi(self):
        output = self._run('print("a b c".toVigintiCaretDelimited())')
        assert output[-1] == "a" + "^" * 20 + "b" + "^" * 20 + "c"
