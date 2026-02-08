"""
Tests for string .toUnderscoreDelimited() method - split words by underscore.
"""

from silk.interpreter import Interpreter


class TestStringToUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toUnderscoreDelimited())')
        assert output[-1] == "hello_world"

    def test_toUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toUnderscoreDelimited())')
        assert output[-1] == "a_b_c"
