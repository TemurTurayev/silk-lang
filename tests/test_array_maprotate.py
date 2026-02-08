"""
Tests for array .mapRotate(n) method - rotate array by n positions.
"""

from silk.interpreter import Interpreter


class TestArrayMapRotate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRotate_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapRotate(1)
print(result)
''')
        assert output[-1] == "[2, 3, 4, 1]"

    def test_mapRotate_two(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapRotate(2)
print(result)
''')
        assert output[-1] == "[3, 4, 5, 1, 2]"
