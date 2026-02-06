"""
Tests for typeof expression.

Syntax: typeof expr  ->  returns string name of type
"""

from silk.interpreter import Interpreter


class TestTypeof:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_typeof_int(self):
        output = self._run('print(typeof 42)')
        assert output[-1] == "int"

    def test_typeof_float(self):
        output = self._run('print(typeof 3.14)')
        assert output[-1] == "float"

    def test_typeof_string(self):
        output = self._run('print(typeof "hello")')
        assert output[-1] == "string"

    def test_typeof_bool(self):
        output = self._run('print(typeof true)')
        assert output[-1] == "bool"

    def test_typeof_null(self):
        output = self._run('print(typeof null)')
        assert output[-1] == "null"

    def test_typeof_array(self):
        output = self._run('print(typeof [1, 2, 3])')
        assert output[-1] == "array"

    def test_typeof_map(self):
        output = self._run('print(typeof {"a": 1})')
        assert output[-1] == "map"

    def test_typeof_function(self):
        output = self._run('''
fn add(a, b) { return a + b }
print(typeof add)
''')
        assert output[-1] == "function"

    def test_typeof_struct(self):
        output = self._run('''
struct Point { x, y }
let p = Point { x: 1, y: 2 }
print(typeof p)
''')
        assert output[-1] == "Point"

    def test_typeof_in_condition(self):
        output = self._run('''
let val = 42
if typeof val == "int" {
    print("is integer")
}
''')
        assert output[-1] == "is integer"

    def test_typeof_variable(self):
        output = self._run('''
let x = "hello"
let t = typeof x
print(t)
''')
        assert output[-1] == "string"
