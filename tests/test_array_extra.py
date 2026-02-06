"""
Tests for array .sort(), .every(), .some() methods.
"""

from silk.interpreter import Interpreter


class TestArraySort:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sort_numbers(self):
        output = self._run('''
let arr = [3, 1, 4, 1, 5, 9]
let sorted = arr.sort()
print(sorted)
''')
        assert output[-1] == "[1, 1, 3, 4, 5, 9]"

    def test_sort_strings(self):
        output = self._run('''
let arr = ["banana", "apple", "cherry"]
let sorted = arr.sort()
print(sorted)
''')
        assert output[-1] == "[apple, banana, cherry]"

    def test_sort_does_not_mutate(self):
        output = self._run('''
let arr = [3, 1, 2]
let sorted = arr.sort()
print(arr)
print(sorted)
''')
        assert output[0] == "[3, 1, 2]"
        assert output[1] == "[1, 2, 3]"

    def test_sort_empty(self):
        output = self._run('''
let arr = []
print(arr.sort())
''')
        assert output[-1] == "[]"

    def test_sort_single(self):
        output = self._run('''
print([42].sort())
''')
        assert output[-1] == "[42]"


class TestArrayEvery:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_every_true(self):
        output = self._run('''
let arr = [2, 4, 6, 8]
let result = arr.every(fn(x) { return x % 2 == 0 })
print(result)
''')
        assert output[-1] == "true"

    def test_every_false(self):
        output = self._run('''
let arr = [2, 3, 6, 8]
let result = arr.every(fn(x) { return x % 2 == 0 })
print(result)
''')
        assert output[-1] == "false"

    def test_every_empty(self):
        output = self._run('''
let arr = []
print(arr.every(fn(x) { return x > 0 }))
''')
        assert output[-1] == "true"


class TestArraySome:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_some_true(self):
        output = self._run('''
let arr = [1, 3, 5, 6]
let result = arr.some(fn(x) { return x % 2 == 0 })
print(result)
''')
        assert output[-1] == "true"

    def test_some_false(self):
        output = self._run('''
let arr = [1, 3, 5, 7]
let result = arr.some(fn(x) { return x % 2 == 0 })
print(result)
''')
        assert output[-1] == "false"

    def test_some_empty(self):
        output = self._run('''
let arr = []
print(arr.some(fn(x) { return x > 0 }))
''')
        assert output[-1] == "false"
