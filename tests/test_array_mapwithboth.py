"""
Tests for array .mapWithBoth(fn) method - map with prev, current, next element.
"""

from silk.interpreter import Interpreter


class TestArrayMapWithBoth:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWithBoth_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapWithBoth(|p, x, n| p + x + n)
print(result)
''')
        assert output[-1] == "[4, 6, 9, 11]"

    def test_mapWithBoth_max(self):
        output = self._run('''
let result = [5, 1, 8, 3].mapWithBoth(|p, x, n| x)
print(result)
''')
        assert output[-1] == "[5, 1, 8, 3]"
