"""
Tests for array .mapBetween(fn) method - apply function between adjacent pairs, returning results.
"""

from silk.interpreter import Interpreter


class TestArrayMapBetween:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBetween_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapBetween(|a, b| a + b)
print(result)
''')
        assert output[-1] == "[3, 5, 7]"

    def test_mapBetween_diff(self):
        output = self._run('''
let result = [10, 5, 20].mapBetween(|a, b| b - a)
print(result)
''')
        assert output[-1] == "[-5, 15]"
