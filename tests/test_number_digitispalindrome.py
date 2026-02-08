"""
Tests for number .digitIsPalindrome() method - check if digits form palindrome.
"""

from silk.interpreter import Interpreter


class TestNumberDigitIsPalindrome:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitIsPalindrome_true(self):
        output = self._run('print(12321.digitIsPalindrome())')
        assert output[-1] == "true"

    def test_digitIsPalindrome_false(self):
        output = self._run('print(12345.digitIsPalindrome())')
        assert output[-1] == "false"
