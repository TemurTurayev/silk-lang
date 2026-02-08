"""
Tests for array .mapZip(other, fn) method - zip two arrays and map.
"""

from silk.interpreter import Interpreter


class TestArrayMapZip:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapZip_add(self):
        output = self._run('''
let result = [1, 2, 3].mapZip([10, 20, 30], |a, b| a + b)
print(result)
''')
        assert output[-1] == "[11, 22, 33]"

    def test_mapZip_multiply(self):
        output = self._run('''
let result = [2, 3].mapZip([4, 5], |a, b| a * b)
print(result)
''')
        assert output[-1] == "[8, 15]"
