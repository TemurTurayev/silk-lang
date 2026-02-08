"""
Tests for number .isPalindromeInBase(base) method - check if palindrome in given base.
"""

from silk.interpreter import Interpreter


class TestNumberIsPalindromeInBase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPalindromeInBase_9_binary(self):
        output = self._run('print(9.isPalindromeInBase(2))')
        assert output[-1] == "true"

    def test_isPalindromeInBase_10_base10(self):
        output = self._run('print(121.isPalindromeInBase(10))')
        assert output[-1] == "true"

    def test_isPalindromeInBase_false(self):
        output = self._run('print(10.isPalindromeInBase(10))')
        assert output[-1] == "false"
