"""
Tests for array .collectMap(fn) method - collect non-null mapped values.
"""

from silk.interpreter import Interpreter


class TestArrayCollectMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_collectMap_double_evens(self):
        output = self._run('''
let result = [1, 2, 3, 4].collectMap(|x| x * 2)
print(result)
''')
        assert output[-1] == "[2, 4, 6, 8]"

    def test_collectMap_square(self):
        output = self._run('''
let result = [3, 4, 5].collectMap(|x| x * x)
print(result)
''')
        assert output[-1] == "[9, 16, 25]"
