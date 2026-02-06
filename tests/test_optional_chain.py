"""
Tests for optional chaining (?.  operator).

Syntax: obj?.field  -> returns null if obj is null, otherwise obj.field
"""

from silk.interpreter import Interpreter


class TestOptionalChaining:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_chain_on_null(self):
        output = self._run('''
let x = null
print(x?.name)
''')
        assert output[-1] == "null"

    def test_chain_on_value(self):
        output = self._run('''
struct User { name }
let u = User { name: "Alice" }
print(u?.name)
''')
        assert output[-1] == "Alice"

    def test_chain_on_struct_field(self):
        output = self._run('''
struct Point { x, y }
let p = Point { x: 10, y: 20 }
print(p?.x)
''')
        assert output[-1] == "10"

    def test_chain_null_object(self):
        output = self._run('''
let p = null
print(p?.x)
''')
        assert output[-1] == "null"

    def test_chain_in_condition(self):
        output = self._run('''
struct Config { host }
let config = null
let host = config?.host ?? "localhost"
print(host)
''')
        assert output[-1] == "localhost"

    def test_chain_on_valid_struct(self):
        output = self._run('''
struct Config { host }
let config = Config { host: "example.com" }
let host = config?.host ?? "localhost"
print(host)
''')
        assert output[-1] == "example.com"
