"""
Tests for null coalescing operator (??).

Syntax: expr ?? default  -> returns expr if not null, otherwise default
"""

from silk.interpreter import Interpreter


class TestNullCoalesce:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_coalesce_null(self):
        output = self._run('''
let x = null
print(x ?? "default")
''')
        assert output[-1] == "default"

    def test_coalesce_value(self):
        output = self._run('''
let x = 42
print(x ?? 0)
''')
        assert output[-1] == "42"

    def test_coalesce_false_not_null(self):
        """false is not null, should not coalesce."""
        output = self._run('''
let x = false
print(x ?? true)
''')
        assert output[-1] == "false"

    def test_coalesce_zero_not_null(self):
        """0 is not null, should not coalesce."""
        output = self._run('''
let x = 0
print(x ?? 99)
''')
        assert output[-1] == "0"

    def test_coalesce_empty_string_not_null(self):
        output = self._run('''
let x = ""
print(x ?? "fallback")
''')
        assert output[-1] == ""

    def test_coalesce_chained(self):
        output = self._run('''
let a = null
let b = null
let c = 42
print(a ?? b ?? c)
''')
        assert output[-1] == "42"

    def test_coalesce_with_function(self):
        output = self._run('''
fn find_user(name) {
    if name == "admin" { return "Admin User" }
    return null
}
let user = find_user("guest") ?? "Unknown"
print(user)
''')
        assert output[-1] == "Unknown"
