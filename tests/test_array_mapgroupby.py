"""
Tests for array .mapGroupBy(fn) method - group elements by function result.
"""

from silk.interpreter import Interpreter


class TestArrayMapGroupBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapGroupBy_modulo(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapGroupBy(|x| x % 2)
print(result)
''')
        assert output[-1] == '{1: [1, 3], 0: [2, 4]}'

    def test_mapGroupBy_identity(self):
        output = self._run('''
let result = [1, 1, 2].mapGroupBy(|x| x)
print(result)
''')
        assert output[-1] == '{1: [1, 1], 2: [2]}'
