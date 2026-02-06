"""
Tests for dict/struct destructuring (let {a, b} = expr).
"""

from silk.interpreter import Interpreter


class TestDictDestructure:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_destructure_map(self):
        output = self._run('''
let m = {"x": 1, "y": 2}
let {x, y} = m
print(x)
print(y)
''')
        assert output[-2] == "1"
        assert output[-1] == "2"

    def test_destructure_struct(self):
        output = self._run('''
struct Point { x, y }
let p = Point { x: 10, y: 20 }
let {x, y} = p
print(x)
print(y)
''')
        assert output[-2] == "10"
        assert output[-1] == "20"

    def test_destructure_partial(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
let {a, c} = m
print(a)
print(c)
''')
        assert output[-2] == "1"
        assert output[-1] == "3"

    def test_destructure_missing_key(self):
        output = self._run('''
let m = {"x": 10}
let {x, y} = m
print(x)
print(y)
''')
        assert output[-2] == "10"
        assert output[-1] == "null"

    def test_destructure_nested_value(self):
        output = self._run('''
let m = {"name": "Alice", "age": 30}
let {name, age} = m
print(f"{name} is {age}")
''')
        assert output[-1] == "Alice is 30"
