"""
Tests for array .mapPrev(fn) method - map with access to previous element.
"""

from silk.interpreter import Interpreter


class TestArrayMapPrev:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPrev_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapPrev(|prev, x| prev + x)
print(result)
''')
        assert output[-1] == "[2, 3, 5, 7]"

    def test_mapPrev_diff(self):
        output = self._run('''
let result = [10, 20, 15, 25].mapPrev(|prev, x| x - prev)
print(result)
''')
        assert output[-1] == "[0, 10, -5, 10]"
