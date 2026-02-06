"""
Tests for array .mapWhile(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayMapWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWhile_basic(self):
        output = self._run('''
fn transform(x) {
    if x < 4 {
        return x * 2
    }
    return false
}
print([1, 2, 3, 4, 5].mapWhile(transform))
''')
        assert output[-1] == "[2, 4, 6]"

    def test_mapWhile_all(self):
        output = self._run('''
fn add1(x) {
    if x < 10 {
        return x + 1
    }
    return false
}
print([1, 2, 3].mapWhile(add1))
''')
        assert output[-1] == "[2, 3, 4]"

    def test_mapWhile_none(self):
        output = self._run('''
fn check(x) {
    if x < 3 {
        return x
    }
    return false
}
print([5, 6, 7].mapWhile(check))
''')
        assert output[-1] == "[]"
