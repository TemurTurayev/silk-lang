"""
Tests for array .mapFlatMap(fn) method - map then flatten.
"""

from silk.interpreter import Interpreter


class TestArrayMapFlatMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFlatMap_duplicate(self):
        output = self._run('''
let result = [1, 2, 3].mapFlatMap(|x| [x, x * 2])
print(result)
''')
        assert output[-1] == "[1, 2, 2, 4, 3, 6]"

    def test_mapFlatMap_single(self):
        output = self._run('''
let result = [5].mapFlatMap(|x| [x, x + 1])
print(result)
''')
        assert output[-1] == "[5, 6]"
