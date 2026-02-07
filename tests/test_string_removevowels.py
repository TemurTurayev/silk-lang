"""
Tests for string .removeVowels() method.
"""

from silk.interpreter import Interpreter


class TestStringRemoveVowels:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_removeVowels_basic(self):
        output = self._run('print("hello".removeVowels())')
        assert output[-1] == "hll"

    def test_removeVowels_all_vowels(self):
        output = self._run('print("aeiou".removeVowels())')
        assert output[-1] == ""
