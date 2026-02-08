"""
Tests for string .toDecCaretDelimited() method - split words by ^^^^^^^^^^ (10 carets).
"""

from silk.interpreter import Interpreter


class TestStringToDecCaretDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecCaretDelimited_basic(self):
        output = self._run('print("hello world".toDecCaretDelimited())')
        assert output[-1] == "hello^^^^^^^^^^world"

    def test_toDecCaretDelimited_three(self):
        output = self._run('print("a b c".toDecCaretDelimited())')
        assert output[-1] == "a^^^^^^^^^^b^^^^^^^^^^c"
