"""
Tests for array .isPalindrome() method - reads same forwards and backwards.
"""

from silk.interpreter import Interpreter


class TestArrayIsPalindrome:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPalindrome_true(self):
        output = self._run('print([1, 2, 3, 2, 1].isPalindrome())')
        assert output[-1] == "true"

    def test_isPalindrome_false(self):
        output = self._run('print([1, 2, 3, 4].isPalindrome())')
        assert output[-1] == "false"
