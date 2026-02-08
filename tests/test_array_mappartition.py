"""
Tests for array .mapPartition(fn) method - split by predicate.
"""

from silk.interpreter import Interpreter


class TestArrayMapPartition:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPartition_gt3(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapPartition(|x| x > 3)
print(result)
''')
        assert output[-1] == "[[4, 5], [1, 2, 3]]"

    def test_mapPartition_even(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapPartition(|x| x % 2 == 0)
print(result)
''')
        assert output[-1] == "[[2, 4], [1, 3]]"
