"""
Tests for array .mapBatch(size, fn) method - process in batches.
"""

from silk.interpreter import Interpreter


class TestArrayMapBatch:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBatch_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5, 6].mapBatch(2, |b| b)
print(result)
''')
        assert output[-1] == "[[1, 2], [3, 4], [5, 6]]"

    def test_mapBatch_single(self):
        output = self._run('''
let result = [1, 2, 3].mapBatch(2, |b| b)
print(result)
''')
        assert output[-1] == "[[1, 2], [3]]"
