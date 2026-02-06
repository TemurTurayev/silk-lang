"""
Tests for array .flat() and .flatMap() methods.
"""

from silk.interpreter import Interpreter


class TestArrayFlat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_flat_basic(self):
        output = self._run('''
let arr = [[1, 2], [3, 4], [5]]
print(arr.flat())
''')
        assert output[-1] == "[1, 2, 3, 4, 5]"

    def test_flat_mixed(self):
        output = self._run('''
let arr = [1, [2, 3], 4, [5, 6]]
print(arr.flat())
''')
        assert output[-1] == "[1, 2, 3, 4, 5, 6]"

    def test_flat_empty(self):
        output = self._run('''
let arr = [[], [], []]
print(arr.flat())
''')
        assert output[-1] == "[]"

    def test_flat_already_flat(self):
        output = self._run('''
let arr = [1, 2, 3]
print(arr.flat())
''')
        assert output[-1] == "[1, 2, 3]"

    def test_flatMap_basic(self):
        output = self._run('''
let arr = [1, 2, 3]
let result = arr.flatMap(fn(x) { return [x, x * 2] })
print(result)
''')
        assert output[-1] == "[1, 2, 2, 4, 3, 6]"

    def test_flatMap_with_lambda(self):
        output = self._run('''
let words = ["hello world", "foo bar"]
let result = words.flatMap(|s| s.split(" "))
print(result)
''')
        assert output[-1] == "[hello, world, foo, bar]"

    def test_flatMap_empty(self):
        output = self._run('''
let arr = []
print(arr.flatMap(fn(x) { return [x] }))
''')
        assert output[-1] == "[]"
