"""
Tests for array .mapReverse(fn) method - map in reverse order.
"""

from silk.interpreter import Interpreter


class TestArrayMapReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapReverse_double(self):
        output = self._run('''
let result = [1, 2, 3].mapReverse(|x| x * 10)
print(result)
''')
        assert output[-1] == "[30, 20, 10]"

    def test_mapReverse_add(self):
        output = self._run('''
let result = [10, 20].mapReverse(|x| x + 1)
print(result)
''')
        assert output[-1] == "[21, 11]"
