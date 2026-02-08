"""
Tests for array .mapUntil(pred, fn) method - map elements until predicate is true.
"""

from silk.interpreter import Interpreter


class TestArrayMapUntil:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapUntil_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapUntil(|x| x > 3, |x| x * 10)
print(result)
''')
        assert output[-1] == "[10, 20, 30, 4, 5]"

    def test_mapUntil_none_match(self):
        output = self._run('''
let result = [1, 2, 3].mapUntil(|x| x > 10, |x| x * 2)
print(result)
''')
        assert output[-1] == "[2, 4, 6]"
