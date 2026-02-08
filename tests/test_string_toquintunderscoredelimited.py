"""
Tests for string .toQuintUnderscoreDelimited() method - split words by _____.
"""

from silk.interpreter import Interpreter


class TestStringToQuintUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toQuintUnderscoreDelimited())')
        assert output[-1] == "hello_____world"

    def test_toQuintUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toQuintUnderscoreDelimited())')
        assert output[-1] == "a_____b_____c"
