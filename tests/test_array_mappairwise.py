"""
Tests for array .mapPairwise(fn) method - map consecutive pairs.
"""

from silk.interpreter import Interpreter


class TestArrayMapPairwise:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPairwise_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapPairwise(|a, b| a + b)
print(result)
''')
        assert output[-1] == "[3, 7]"

    def test_mapPairwise_multiply(self):
        output = self._run('''
let result = [2, 3, 4, 5].mapPairwise(|a, b| a * b)
print(result)
''')
        assert output[-1] == "[6, 20]"
