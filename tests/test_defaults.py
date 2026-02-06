"""
Tests for default parameter values.

Syntax: fn greet(name, greeting = "Hello") { ... }
"""

import pytest
from silk.lexer import Lexer
from silk.parser import Parser
from silk.interpreter import Interpreter


class TestDefaultParams:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_default(self):
        output = self._run('''
fn greet(name, greeting = "Hello") {
    print(f"{greeting}, {name}!")
}
greet("Alice")
''')
        assert output[-1] == "Hello, Alice!"

    def test_override_default(self):
        output = self._run('''
fn greet(name, greeting = "Hello") {
    print(f"{greeting}, {name}!")
}
greet("Bob", "Hi")
''')
        assert output[-1] == "Hi, Bob!"

    def test_multiple_defaults(self):
        output = self._run('''
fn config(host = "localhost", port = 8080) {
    print(f"{host}:{port}")
}
config()
''')
        assert output[-1] == "localhost:8080"

    def test_partial_defaults(self):
        output = self._run('''
fn config(host = "localhost", port = 8080) {
    print(f"{host}:{port}")
}
config("example.com")
''')
        assert output[-1] == "example.com:8080"

    def test_all_overridden(self):
        output = self._run('''
fn config(host = "localhost", port = 8080) {
    print(f"{host}:{port}")
}
config("example.com", 3000)
''')
        assert output[-1] == "example.com:3000"

    def test_numeric_default(self):
        output = self._run('''
fn power(base, exp = 2) {
    return base ** exp
}
print(power(3))
print(power(3, 3))
''')
        assert output[0] == "9"
        assert output[1] == "27"

    def test_bool_default(self):
        output = self._run('''
fn log(msg, verbose = false) {
    if verbose {
        print(f"[VERBOSE] {msg}")
    } else {
        print(msg)
    }
}
log("hello")
log("hello", true)
''')
        assert output[0] == "hello"
        assert output[1] == "[VERBOSE] hello"

    def test_null_default(self):
        output = self._run('''
fn maybe(val = null) {
    if val == null then print("nothing") else print(val)
}
maybe()
maybe(42)
''')
        assert output[0] == "nothing"
        assert output[1] == "42"

    def test_default_with_required_before(self):
        output = self._run('''
fn format(value, prefix = "", suffix = "") {
    print(f"{prefix}{value}{suffix}")
}
format(42)
format(42, "$")
format(42, "$", "!")
''')
        assert output[0] == "42"
        assert output[1] == "$42"
        assert output[2] == "$42!"
