"""
Tests for array .mapAsync(fn) method - async-style map (alias for map).
"""

from silk.interpreter import Interpreter


class TestArrayMapAsync:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAsync_double(self):
        output = self._run('''
let result = [1, 2, 3].mapAsync(|x| x * 2)
print(result)
''')
        assert output[-1] == "[2, 4, 6]"

    def test_mapAsync_add(self):
        output = self._run('''
let result = [10, 20].mapAsync(|x| x + 1)
print(result)
''')
        assert output[-1] == "[11, 21]"
