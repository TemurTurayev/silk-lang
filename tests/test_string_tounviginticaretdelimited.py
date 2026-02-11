"""
Tests for string .toUnvigintiCaretDelimited() method - join words with 21 carets.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiCaretDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiCaretDelimited())')
        assert output[-1] == "hello" + "^" * 21 + "world"

    def test_toUnvigintiCaretDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiCaretDelimited())')
        assert output[-1] == "a" + "^" * 21 + "b" + "^" * 21 + "c"
