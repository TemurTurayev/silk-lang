"""
Tests for array .suffixes() method.
"""

from silk.interpreter import Interpreter


class TestArraySuffixes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_suffixes_basic(self):
        output = self._run('print([1, 2, 3].suffixes())')
        assert output[-1] == "[[1, 2, 3], [2, 3], [3]]"

    def test_suffixes_single(self):
        output = self._run('print([1].suffixes())')
        assert output[-1] == "[[1]]"

    def test_suffixes_empty(self):
        output = self._run('print([].suffixes())')
        assert output[-1] == "[]"
