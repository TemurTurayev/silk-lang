"""
Tests for string .countWords(word) method.
"""

from silk.interpreter import Interpreter


class TestStringCountWords:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countWords_basic(self):
        output = self._run('print("the cat and the dog".countWords("the"))')
        assert output[-1] == "2"

    def test_countWords_none(self):
        output = self._run('print("hello world".countWords("foo"))')
        assert output[-1] == "0"

    def test_countWords_one(self):
        output = self._run('print("hello world hello".countWords("world"))')
        assert output[-1] == "1"
