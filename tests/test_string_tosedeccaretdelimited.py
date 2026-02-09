"""
Tests for string .toSedecCaretDelimited() method - join words with 16 carets.
"""

from silk.interpreter import Interpreter


class TestStringToSedecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecCaretDelimited_basic(self):
        output = self._run('print("hello world".toSedecCaretDelimited())')
        assert output[-1] == "hello" + "^" * 16 + "world"

    def test_toSedecCaretDelimited_three(self):
        output = self._run('print("a b c".toSedecCaretDelimited())')
        assert output[-1] == "a" + "^" * 16 + "b" + "^" * 16 + "c"
