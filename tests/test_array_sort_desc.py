"""
Tests for array .sortDescending() and .forEachIndexed() methods.
"""

from silk.interpreter import Interpreter


class TestArraySortDesc:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sortDescending_basic(self):
        output = self._run('''
print([3, 1, 4, 1, 5].sortDescending())
''')
        assert output[-1] == "[5, 4, 3, 1, 1]"

    def test_sortDescending_already_sorted(self):
        output = self._run('''
print([5, 4, 3, 2, 1].sortDescending())
''')
        assert output[-1] == "[5, 4, 3, 2, 1]"

    def test_sortDescending_single(self):
        output = self._run('''
print([1].sortDescending())
''')
        assert output[-1] == "[1]"


class TestArrayForEachIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_forEachIndexed_basic(self):
        output = self._run('''
let mut result = []
["a", "b", "c"].forEachIndexed(fn(i, v) {
    result.push(f"{i}={v}")
})
print(result)
''')
        assert output[-1] == "[0=a, 1=b, 2=c]"
