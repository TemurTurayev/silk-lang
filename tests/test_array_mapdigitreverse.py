"""
Tests for array .mapDigitReverse() method - reverse digits of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitReverse_basic(self):
        output = self._run('print([123, 456, 789].mapDigitReverse())')
        assert output[-1] == "[321, 654, 987]"

    def test_mapDigitReverse_palindrome(self):
        output = self._run('print([121, 5, 100].mapDigitReverse())')
        assert output[-1] == "[121, 5, 1]"
