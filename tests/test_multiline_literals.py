"""
Tests for multi-line array, map, and struct literals.
"""

from silk.interpreter import Interpreter


class TestMultilineArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_multiline_array(self):
        output = self._run('''
let arr = [
    1,
    2,
    3
]
print(arr)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_multiline_array_trailing_comma(self):
        output = self._run('''
let arr = [
    "a",
    "b",
    "c",
]
print(arr.length)
''')
        assert output[-1] == "3"

    def test_multiline_array_nested(self):
        output = self._run('''
let matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[0])
print(matrix[1])
''')
        assert output[-2] == "[1, 2]"
        assert output[-1] == "[3, 4]"


class TestMultilineMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_multiline_map(self):
        output = self._run('''
let m = {
    "name": "Alice",
    "age": 30
}
print(m["name"])
print(m["age"])
''')
        assert output[-2] == "Alice"
        assert output[-1] == "30"

    def test_multiline_map_trailing_comma(self):
        output = self._run('''
let m = {
    "x": 1,
    "y": 2,
}
print(m.length)
''')
        assert output[-1] == "2"


class TestMultilineStruct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_multiline_struct_instance(self):
        output = self._run('''
struct User { name, age, email }
let u = User {
    name: "Alice",
    age: 30,
    email: "alice@example.com"
}
print(u.name)
print(u.age)
''')
        assert output[-2] == "Alice"
        assert output[-1] == "30"

    def test_multiline_fn_args(self):
        output = self._run('''
fn add(
    a,
    b
) {
    return a + b
}
print(add(1, 2))
''')
        assert output[-1] == "3"

    def test_multiline_fn_call_args(self):
        output = self._run('''
fn sum3(a, b, c) {
    return a + b + c
}
let result = sum3(
    10,
    20,
    30
)
print(result)
''')
        assert output[-1] == "60"
