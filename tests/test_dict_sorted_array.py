"""
Tests for dict .toSortedArray() method.
"""

from silk.interpreter import Interpreter


class TestDictToSortedArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSortedArray_basic(self):
        output = self._run('''
let d = {"c": 3, "a": 1, "b": 2}
let arr = d.toSortedArray()
print(arr[0])
print(arr[1])
print(arr[2])
''')
        assert output[0] == "[a, 1]"
        assert output[1] == "[b, 2]"
        assert output[2] == "[c, 3]"

    def test_toSortedArray_empty(self):
        output = self._run('''
let d = {"a": 1}
let e = d.filter(|k, v| false)
print(e.toSortedArray())
''')
        assert output[-1] == "[]"

    def test_toSortedArray_single(self):
        output = self._run('''
let d = {"x": 42}
print(d.toSortedArray())
''')
        assert output[-1] == "[[x, 42]]"
