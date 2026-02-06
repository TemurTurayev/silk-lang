"""
Tests for struct field assignment (member assignment).

Syntax: obj.field = value
Requires the struct variable to be declared as `let mut`.
"""

import pytest
from silk.interpreter import Interpreter
from silk.errors import RuntimeError_


class TestFieldAssign:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_field_assign(self):
        output = self._run('''
struct Point { x, y }
let mut p = Point { x: 1, y: 2 }
p.x = 10
print(p.x)
''')
        assert output[-1] == "10"

    def test_multiple_field_assigns(self):
        output = self._run('''
struct Point { x, y }
let mut p = Point { x: 0, y: 0 }
p.x = 3
p.y = 4
print(p)
''')
        assert output[-1] == "Point { x: 3, y: 4 }"

    def test_field_assign_string(self):
        output = self._run('''
struct User { name, email }
let mut user = User { name: "Alice", email: "a@b.com" }
user.email = "alice@new.com"
print(user.email)
''')
        assert output[-1] == "alice@new.com"

    def test_field_assign_in_method(self):
        output = self._run('''
struct Counter { count }
impl Counter {
    fn increment(self) {
        self.count = self.count + 1
    }
    fn get(self) {
        return self.count
    }
}
let mut c = Counter { count: 0 }
c.increment()
c.increment()
c.increment()
print(c.get())
''')
        assert output[-1] == "3"

    def test_field_assign_preserves_other_fields(self):
        output = self._run('''
struct RGB { r, g, b }
let mut color = RGB { r: 255, g: 128, b: 0 }
color.g = 200
print(color.r)
print(color.g)
print(color.b)
''')
        assert output[0] == "255"
        assert output[1] == "200"
        assert output[2] == "0"

    def test_field_assign_computed_value(self):
        output = self._run('''
struct Score { value }
let mut s = Score { value: 10 }
s.value = s.value * 2 + 5
print(s.value)
''')
        assert output[-1] == "25"

    def test_nested_field_access_after_assign(self):
        output = self._run('''
struct Config { host, port }
let mut cfg = Config { host: "localhost", port: 8080 }
cfg.port = 3000
print(f"{cfg.host}:{cfg.port}")
''')
        assert output[-1] == "localhost:3000"
