"""
Tests for array .mapOnly(indices, fn) method - map only at given indices.
"""

from silk.interpreter import Interpreter


class TestArrayMapOnly:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapOnly_indices(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapOnly([1, 3], |x| x * 10)
print(result)
''')
        assert output[-1] == "[1, 20, 3, 40]"

    def test_mapOnly_first(self):
        output = self._run('''
let result = [10, 20, 30].mapOnly([0], |x| x + 1)
print(result)
''')
        assert output[-1] == "[11, 20, 30]"
