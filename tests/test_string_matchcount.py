"""
Tests for string .matchCount(pattern) method.
"""

from silk.interpreter import Interpreter


class TestStringMatchCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_matchCount_digits(self):
        output = self._run(r'print("abc123def456".matchCount("\d+"))')
        assert output[-1] == "2"

    def test_matchCount_words(self):
        output = self._run(r'print("hello world foo".matchCount("\w+"))')
        assert output[-1] == "3"

    def test_matchCount_none(self):
        output = self._run(r'print("hello".matchCount("\d+"))')
        assert output[-1] == "0"
