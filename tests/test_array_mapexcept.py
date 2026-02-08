"""
Tests for array .mapExcept(indices, fn) method - map all except at indices.
"""

from silk.interpreter import Interpreter


class TestArrayMapExcept:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapExcept_skip_index1(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapExcept([1], |x| x * 10)
print(result)
''')
        assert output[-1] == "[10, 2, 30, 40]"

    def test_mapExcept_skip_ends(self):
        output = self._run('''
let result = [10, 20, 30].mapExcept([0, 2], |x| x + 1)
print(result)
''')
        assert output[-1] == "[10, 21, 30]"
