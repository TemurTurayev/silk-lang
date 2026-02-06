"""
Tests for dict .sortByValue() method.
"""

from silk.interpreter import Interpreter


class TestDictSortByValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sortByValue_basic(self):
        output = self._run('''
let d = {"c": 3, "a": 1, "b": 2}
let arr = d.sortByValue()
print(arr[0])
print(arr[1])
print(arr[2])
''')
        assert output[0] == "[a, 1]"
        assert output[1] == "[b, 2]"
        assert output[2] == "[c, 3]"

    def test_sortByValue_single(self):
        output = self._run('''
let d = {"x": 42}
print(d.sortByValue())
''')
        assert output[-1] == "[[x, 42]]"
