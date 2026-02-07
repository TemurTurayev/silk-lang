"""
Tests for string .occurrences(sub) method - returns indices of all occurrences.
"""

from silk.interpreter import Interpreter


class TestStringOccurrences:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_occurrences_basic(self):
        output = self._run('print("abcabc".occurrences("a"))')
        assert output[-1] == "[0, 3]"

    def test_occurrences_none(self):
        output = self._run('print("hello".occurrences("z"))')
        assert output[-1] == "[]"
