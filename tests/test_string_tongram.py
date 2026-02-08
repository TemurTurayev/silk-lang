"""
Tests for string .toNGram(n) method - split into character n-grams.
"""

from silk.interpreter import Interpreter


class TestStringToNGram:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNGram_bigrams(self):
        output = self._run('print("hello".toNGram(2))')
        assert output[-1] == '[he, el, ll, lo]'

    def test_toNGram_trigrams(self):
        output = self._run('print("abcde".toNGram(3))')
        assert output[-1] == '[abc, bcd, cde]'
