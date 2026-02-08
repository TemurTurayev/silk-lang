"""
Tests for array .mapSkip(n, fn) method - skip first n elements, map rest.
"""

from silk.interpreter import Interpreter


class TestArrayMapSkip:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSkip_2(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapSkip(2, |x| x * 10)
print(result)
''')
        assert output[-1] == "[1, 2, 30, 40]"

    def test_mapSkip_1(self):
        output = self._run('''
let result = [5, 10, 15].mapSkip(1, |x| x + 1)
print(result)
''')
        assert output[-1] == "[5, 11, 16]"
