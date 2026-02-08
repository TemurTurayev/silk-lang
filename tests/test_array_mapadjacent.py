"""
Tests for array .mapAdjacent(n, fn) method - map over windows of n adjacent elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapAdjacent:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAdjacent_sum_pairs(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapAdjacent(2, |a, b| a + b)
print(result)
''')
        assert output[-1] == "[3, 5, 7]"

    def test_mapAdjacent_triple(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapAdjacent(3, |a, b, c| a + b + c)
print(result)
''')
        assert output[-1] == "[6, 9, 12]"
