"""
Tests for array .mapWithIndex(fn) method - map with index as first arg.
"""

from silk.interpreter import Interpreter


class TestArrayMapWithIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWithIndex_add(self):
        output = self._run('''
let result = [10, 20, 30].mapWithIndex(|i, x| i + x)
print(result)
''')
        assert output[-1] == "[10, 21, 32]"

    def test_mapWithIndex_multiply(self):
        output = self._run('''
let result = [5, 5, 5].mapWithIndex(|i, x| i * x)
print(result)
''')
        assert output[-1] == "[0, 5, 10]"
