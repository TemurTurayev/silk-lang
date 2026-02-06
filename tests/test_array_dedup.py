"""
Tests for array .dedup() method.
"""

from silk.interpreter import Interpreter


class TestArrayDedup:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dedup_basic(self):
        output = self._run('print([1, 1, 2, 2, 3, 1, 1].dedup())')
        assert output[-1] == "[1, 2, 3, 1]"

    def test_dedup_no_dupes(self):
        output = self._run('print([1, 2, 3].dedup())')
        assert output[-1] == "[1, 2, 3]"

    def test_dedup_all_same(self):
        output = self._run('print([5, 5, 5].dedup())')
        assert output[-1] == "[5]"
