"""
Tests for string .toReverse() method - reverse the string (alias for reverse).
"""

from silk.interpreter import Interpreter


class TestStringToReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toReverse_basic(self):
        output = self._run('print("hello".toReverse())')
        assert output[-1] == "olleh"

    def test_toReverse_palindrome(self):
        output = self._run('print("aba".toReverse())')
        assert output[-1] == "aba"
