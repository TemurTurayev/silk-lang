"""
Tests for array .maxIndex() and .minIndex() methods.
"""

from silk.interpreter import Interpreter


class TestArrayMaxMinIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_maxIndex_basic(self):
        output = self._run('print([3, 7, 2, 9, 1].maxIndex())')
        assert output[-1] == "3"

    def test_minIndex_basic(self):
        output = self._run('print([3, 7, 2, 9, 1].minIndex())')
        assert output[-1] == "4"
