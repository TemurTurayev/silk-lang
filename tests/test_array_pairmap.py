"""
Tests for array .pairMap(fn) method - map over consecutive pairs.
"""

from silk.interpreter import Interpreter


class TestArrayPairMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pairMap_sum(self):
        output = self._run('print([1, 2, 3, 4].pairMap(|a, b| a + b))')
        assert output[-1] == "[3, 5, 7]"

    def test_pairMap_diff(self):
        output = self._run('print([10, 7, 3].pairMap(|a, b| a - b))')
        assert output[-1] == "[3, 4]"

    def test_pairMap_single(self):
        output = self._run('print([1].pairMap(|a, b| a + b))')
        assert output[-1] == "[]"
