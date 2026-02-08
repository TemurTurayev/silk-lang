"""
Tests for array .mapChunked(n, fn) method - chunk then map each chunk.
"""

from silk.interpreter import Interpreter


class TestArrayMapChunked:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapChunked_sum_pairs(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapChunked(2, |a, b| a + b)
print(result)
''')
        assert output[-1] == "[3, 7]"

    def test_mapChunked_triple(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5, 6].mapChunked(3, |a, b, c| a + b + c)
print(result)
''')
        assert output[-1] == "[6, 15]"
