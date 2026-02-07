"""
Tests for string .countConsonants() method.
"""

from silk.interpreter import Interpreter


class TestStringCountConsonants:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countConsonants_basic(self):
        output = self._run('print("hello world".countConsonants())')
        assert output[-1] == "7"

    def test_countConsonants_vowels_only(self):
        output = self._run('print("aeiou".countConsonants())')
        assert output[-1] == "0"
