"""
Tests for string .reverse() and .isEmpty() methods.
"""

from silk.interpreter import Interpreter


class TestStringReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reverse_basic(self):
        output = self._run('print("hello".reverse())')
        assert output[-1] == "olleh"

    def test_reverse_palindrome(self):
        output = self._run('''
let s = "racecar"
print(s == s.reverse())
''')
        assert output[-1] == "true"

    def test_reverse_empty(self):
        output = self._run('print("".reverse())')
        assert output[-1] == ""

    def test_reverse_single_char(self):
        output = self._run('print("x".reverse())')
        assert output[-1] == "x"


class TestStringIsEmpty:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEmpty_empty(self):
        output = self._run('print("".isEmpty())')
        assert output[-1] == "true"

    def test_isEmpty_nonempty(self):
        output = self._run('print("hello".isEmpty())')
        assert output[-1] == "false"

    def test_isEmpty_whitespace(self):
        output = self._run('print(" ".isEmpty())')
        assert output[-1] == "false"

    def test_isEmpty_after_trim(self):
        output = self._run('print("   ".trim().isEmpty())')
        assert output[-1] == "true"
