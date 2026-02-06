"""
Tests for array .unique() and .count() methods.
"""

from silk.interpreter import Interpreter


class TestArrayUnique:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_unique_basic(self):
        output = self._run('''
let arr = [1, 2, 2, 3, 3, 3]
print(arr.unique())
''')
        assert output[-1] == "[1, 2, 3]"

    def test_unique_strings(self):
        output = self._run('''
let arr = ["a", "b", "a", "c", "b"]
print(arr.unique())
''')
        assert output[-1] == "[a, b, c]"

    def test_unique_already_unique(self):
        output = self._run('''
print([1, 2, 3].unique())
''')
        assert output[-1] == "[1, 2, 3]"

    def test_unique_empty(self):
        output = self._run('''
print([].unique())
''')
        assert output[-1] == "[]"

    def test_unique_preserves_order(self):
        output = self._run('''
let arr = [3, 1, 2, 1, 3]
print(arr.unique())
''')
        assert output[-1] == "[3, 1, 2]"


class TestArrayCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_count_basic(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
print(arr.count(|x| x > 3))
''')
        assert output[-1] == "2"

    def test_count_all(self):
        output = self._run('''
print([1, 2, 3].count(|x| x > 0))
''')
        assert output[-1] == "3"

    def test_count_none(self):
        output = self._run('''
print([1, 2, 3].count(|x| x > 10))
''')
        assert output[-1] == "0"

    def test_count_empty(self):
        output = self._run('''
print([].count(|x| x > 0))
''')
        assert output[-1] == "0"
