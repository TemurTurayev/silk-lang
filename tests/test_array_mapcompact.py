"""
Tests for array .mapCompact() method - remove null/0/false values.
"""

from silk.interpreter import Interpreter


class TestArrayMapCompact:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCompact_with_nulls(self):
        output = self._run('print([1, null, 2, null, 3].mapCompact())')
        assert output[-1] == "[1, 2, 3]"

    def test_mapCompact_with_zeros(self):
        output = self._run('print([0, 1, 0, 2].mapCompact())')
        assert output[-1] == "[1, 2]"
