"""
Tests for destructuring let on arrays.

Syntax: let [a, b, c] = expr
"""

from silk.interpreter import Interpreter


class TestArrayDestructure:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_destructure(self):
        output = self._run('''
let [a, b, c] = [1, 2, 3]
print(a)
print(b)
print(c)
''')
        assert output == ["1", "2", "3"]

    def test_destructure_from_variable(self):
        output = self._run('''
let arr = [10, 20, 30]
let [x, y, z] = arr
print(x + y + z)
''')
        assert output[-1] == "60"

    def test_destructure_partial(self):
        """Take fewer elements than array has."""
        output = self._run('''
let [first, second] = [1, 2, 3, 4, 5]
print(first)
print(second)
''')
        assert output == ["1", "2"]

    def test_destructure_with_rest(self):
        """Use spread to capture remaining elements."""
        output = self._run('''
let [head, ...tail] = [1, 2, 3, 4, 5]
print(head)
print(tail)
''')
        assert output[0] == "1"
        assert output[1] == "[2, 3, 4, 5]"

    def test_destructure_function_return(self):
        output = self._run('''
fn min_max(arr) {
    let mut lo = arr[0]
    let mut hi = arr[0]
    for x in arr {
        if x < lo { lo = x }
        if x > hi { hi = x }
    }
    return [lo, hi]
}
let [lo, hi] = min_max([3, 1, 4, 1, 5, 9])
print(lo)
print(hi)
''')
        assert output[0] == "1"
        assert output[1] == "9"

    def test_destructure_swap(self):
        output = self._run('''
let mut a = 1
let mut b = 2
let [x, y] = [b, a]
a = x
b = y
print(a)
print(b)
''')
        assert output[0] == "2"
        assert output[1] == "1"

    def test_destructure_nested_expression(self):
        output = self._run('''
let [a, b] = [1 + 2, 3 * 4]
print(a)
print(b)
''')
        assert output[0] == "3"
        assert output[1] == "12"
