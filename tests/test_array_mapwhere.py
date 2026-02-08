"""
Tests for array .mapWhere(pred, fn) method - map only where predicate is true.
"""

from silk.interpreter import Interpreter


class TestArrayMapWhere:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWhere_double_evens(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapWhere(|x| x % 2 == 0, |x| x * 10)
print(result)
''')
        assert output[-1] == "[1, 20, 3, 40]"

    def test_mapWhere_negate_positive(self):
        output = self._run('''
let result = [5, -3, 8].mapWhere(|x| x > 0, |x| 0 - x)
print(result)
''')
        assert output[-1] == "[-5, -3, -8]"
