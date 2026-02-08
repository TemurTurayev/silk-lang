"""
Tests for array .mapFlat(fn) method - map and flatten result.
"""

from silk.interpreter import Interpreter


class TestArrayMapFlat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFlat_duplicate(self):
        output = self._run('''
let result = [1, 2, 3].mapFlat(|x| [x, x * 2])
print(result)
''')
        assert output[-1] == "[1, 2, 2, 4, 3, 6]"

    def test_mapFlat_split(self):
        output = self._run('''
let result = [10, 20].mapFlat(|x| [x - 1, x, x + 1])
print(result)
''')
        assert output[-1] == "[9, 10, 11, 19, 20, 21]"
