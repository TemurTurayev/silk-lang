"""
Tests for array .mapWithNext(fn) method - map with next element.
"""

from silk.interpreter import Interpreter


class TestArrayMapWithNext:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWithNext_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapWithNext(|a, b| a + b)
print(result)
''')
        assert output[-1] == "[3, 5, 7]"

    def test_mapWithNext_diff(self):
        output = self._run('''
let result = [10, 7, 3].mapWithNext(|a, b| a - b)
print(result)
''')
        assert output[-1] == "[3, 4]"
