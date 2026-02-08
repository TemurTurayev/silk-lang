"""
Tests for array .mapEnumerate() method - wrap each element with its index.
"""

from silk.interpreter import Interpreter


class TestArrayMapEnumerate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapEnumerate_basic(self):
        output = self._run('''
let result = [10, 20, 30].mapEnumerate()
print(result)
''')
        assert output[-1] == "[[0, 10], [1, 20], [2, 30]]"

    def test_mapEnumerate_strings(self):
        output = self._run('''
let result = ["a", "b"].mapEnumerate()
print(result)
''')
        assert output[-1] == '[[0, a], [1, b]]'
