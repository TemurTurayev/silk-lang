"""
Tests for array .mapZipWith(other) method - zip two arrays into pairs.
"""

from silk.interpreter import Interpreter


class TestArrayMapZipWith:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapZipWith_basic(self):
        output = self._run('''
let result = [1, 2, 3].mapZipWith([4, 5, 6])
print(result)
''')
        assert output[-1] == "[[1, 4], [2, 5], [3, 6]]"

    def test_mapZipWith_uneven(self):
        output = self._run('''
let result = [1, 2].mapZipWith([3, 4, 5])
print(result)
''')
        assert output[-1] == "[[1, 3], [2, 4]]"
