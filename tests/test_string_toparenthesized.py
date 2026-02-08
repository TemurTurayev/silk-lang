"""
Tests for string .toParenthesized() method - wrap string in parentheses.
"""

from silk.interpreter import Interpreter


class TestStringToParenthesized:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toParenthesized_basic(self):
        output = self._run('print("hello".toParenthesized())')
        assert output[-1] == "(hello)"

    def test_toParenthesized_word(self):
        output = self._run('print("test".toParenthesized())')
        assert output[-1] == "(test)"
