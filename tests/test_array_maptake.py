"""
Tests for array .mapTake(n, fn) method - map only first n elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapTake:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTake_2(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapTake(2, |x| x * 10)
print(result)
''')
        assert output[-1] == "[10, 20, 3, 4]"

    def test_mapTake_1(self):
        output = self._run('''
let result = [5, 10, 15].mapTake(1, |x| x + 1)
print(result)
''')
        assert output[-1] == "[6, 10, 15]"
