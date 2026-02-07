"""
Tests for string .countVowels() method.
"""

from silk.interpreter import Interpreter


class TestStringCountVowels:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countVowels_basic(self):
        output = self._run('print("hello world".countVowels())')
        assert output[-1] == "3"

    def test_countVowels_none(self):
        output = self._run('print("xyz".countVowels())')
        assert output[-1] == "0"

    def test_countVowels_all(self):
        output = self._run('print("aeiou".countVowels())')
        assert output[-1] == "5"
