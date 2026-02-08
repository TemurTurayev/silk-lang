"""
Tests for string .toNonUnderscoreDelimited() method - split words by _________ (9 underscores).
"""

from silk.interpreter import Interpreter


class TestStringToNonUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toNonUnderscoreDelimited())')
        assert output[-1] == "hello_________world"

    def test_toNonUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toNonUnderscoreDelimited())')
        assert output[-1] == "a_________b_________c"
