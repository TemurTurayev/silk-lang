"""
Tests for string .levenshtein() method.
"""

from silk.interpreter import Interpreter


class TestStringLevenshtein:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_levenshtein_same(self):
        output = self._run('print("hello".levenshtein("hello"))')
        assert output[-1] == "0"

    def test_levenshtein_one_edit(self):
        output = self._run('print("kitten".levenshtein("sitten"))')
        assert output[-1] == "1"

    def test_levenshtein_multi(self):
        output = self._run('print("kitten".levenshtein("sitting"))')
        assert output[-1] == "3"

    def test_levenshtein_empty(self):
        output = self._run('print("".levenshtein("abc"))')
        assert output[-1] == "3"
