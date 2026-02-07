"""
Tests for string .removeDuplicateChars() method.
"""

from silk.interpreter import Interpreter


class TestStringRemoveDuplicateChars:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_removeDuplicateChars_basic(self):
        output = self._run('print("aabbccdd".removeDuplicateChars())')
        assert output[-1] == "abcd"

    def test_removeDuplicateChars_mixed(self):
        output = self._run('print("aabba".removeDuplicateChars())')
        assert output[-1] == "aba"

    def test_removeDuplicateChars_none(self):
        output = self._run('print("abc".removeDuplicateChars())')
        assert output[-1] == "abc"
