"""
Tests for spread operator in array literals.

Syntax: [...a, ...b, elem]
"""

from silk.interpreter import Interpreter


class TestSpreadOperator:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_spread_single_array(self):
        output = self._run('''
let a = [1, 2, 3]
let b = [...a]
print(b)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_spread_concat_two_arrays(self):
        output = self._run('''
let a = [1, 2]
let b = [3, 4]
let c = [...a, ...b]
print(c)
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_spread_with_extra_elements(self):
        output = self._run('''
let a = [2, 3]
let result = [1, ...a, 4, 5]
print(result)
''')
        assert output[-1] == "[1, 2, 3, 4, 5]"

    def test_spread_empty_array(self):
        output = self._run('''
let a = []
let b = [1, ...a, 2]
print(b)
''')
        assert output[-1] == "[1, 2]"

    def test_spread_preserves_original(self):
        output = self._run('''
let a = [1, 2, 3]
let b = [...a, 4]
print(a)
print(b)
''')
        assert output[0] == "[1, 2, 3]"
        assert output[1] == "[1, 2, 3, 4]"

    def test_spread_nested(self):
        output = self._run('''
let a = [1, 2]
let b = [3, 4]
let c = [0, ...a, ...b, 5]
print(c)
print(c.length)
''')
        assert output[0] == "[0, 1, 2, 3, 4, 5]"
        assert output[1] == "6"

    def test_spread_in_function_return(self):
        output = self._run('''
fn merge(a, b) {
    return [...a, ...b]
}
let result = merge([1, 2], [3, 4])
print(result)
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_spread_string_chars(self):
        output = self._run('''
let chars = "hi".chars()
let arr = [0, ...chars]
print(arr)
''')
        assert output[-1] == "[0, h, i]"
