"""
Tests for array .foldMap(fn) method - map then fold (sum mapped results).
"""

from silk.interpreter import Interpreter


class TestArrayFoldMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_foldMap_double(self):
        output = self._run('''
let result = [1, 2, 3].foldMap(|x| x * 2)
print(result)
''')
        assert output[-1] == "12"

    def test_foldMap_square(self):
        output = self._run('''
let result = [2, 3, 4].foldMap(|x| x * x)
print(result)
''')
        assert output[-1] == "29"
