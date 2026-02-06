"""
Tests for array .prefixes() method.
"""

from silk.interpreter import Interpreter


class TestArrayPrefixes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_prefixes_basic(self):
        output = self._run('print([1, 2, 3].prefixes())')
        assert output[-1] == "[[1], [1, 2], [1, 2, 3]]"

    def test_prefixes_single(self):
        output = self._run('print([1].prefixes())')
        assert output[-1] == "[[1]]"

    def test_prefixes_empty(self):
        output = self._run('print([].prefixes())')
        assert output[-1] == "[]"
