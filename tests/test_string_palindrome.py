"""
Tests for string .isPalindrome() method.
"""

from silk.interpreter import Interpreter


class TestStringIsPalindrome:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPalindrome_true(self):
        output = self._run('print("racecar".isPalindrome())')
        assert output[-1] == "true"

    def test_isPalindrome_false(self):
        output = self._run('print("hello".isPalindrome())')
        assert output[-1] == "false"

    def test_isPalindrome_single(self):
        output = self._run('print("a".isPalindrome())')
        assert output[-1] == "true"

    def test_isPalindrome_empty(self):
        output = self._run('print("".isPalindrome())')
        assert output[-1] == "true"
