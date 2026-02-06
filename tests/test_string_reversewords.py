"""
Tests for string .reverseWords() method.
"""

from silk.interpreter import Interpreter


class TestStringReverseWords:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reverseWords_basic(self):
        output = self._run('print("hello world foo".reverseWords())')
        assert output[-1] == "foo world hello"

    def test_reverseWords_single(self):
        output = self._run('print("hello".reverseWords())')
        assert output[-1] == "hello"

    def test_reverseWords_empty(self):
        output = self._run('print("".reverseWords())')
        assert output[-1] == ""
