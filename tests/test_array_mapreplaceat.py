"""
Tests for array .mapReplaceAt(index, value) method - replace element at index.
"""

from silk.interpreter import Interpreter


class TestArrayMapReplaceAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapReplaceAt_middle(self):
        output = self._run('print([1, 2, 3].mapReplaceAt(1, 99))')
        assert output[-1] == "[1, 99, 3]"

    def test_mapReplaceAt_first(self):
        output = self._run('print([10, 20, 30].mapReplaceAt(0, 0))')
        assert output[-1] == "[0, 20, 30]"
