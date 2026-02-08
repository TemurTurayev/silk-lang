"""
Tests for array .mapDropWhile(fn) method - drop elements while predicate true.
"""

from silk.interpreter import Interpreter


class TestArrayMapDropWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDropWhile_lessThan3(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapDropWhile(|x| x < 3)
print(result)
''')
        assert output[-1] == "[3, 4, 5]"

    def test_mapDropWhile_none(self):
        output = self._run('''
let result = [5, 6, 7].mapDropWhile(|x| x < 3)
print(result)
''')
        assert output[-1] == "[5, 6, 7]"
