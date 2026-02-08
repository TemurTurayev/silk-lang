"""
Tests for array .mapChunkEvery(n) method - split into chunks of size n.
"""

from silk.interpreter import Interpreter


class TestArrayMapChunkEvery:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapChunkEvery_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapChunkEvery(2)
print(result)
''')
        assert output[-1] == "[[1, 2], [3, 4], [5]]"

    def test_mapChunkEvery_exact(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapChunkEvery(2)
print(result)
''')
        assert output[-1] == "[[1, 2], [3, 4]]"
