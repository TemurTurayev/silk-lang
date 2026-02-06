"""
Tests for forEach builtin and array method.

Syntax:
  forEach(array, fn(item) { ... })
  array.forEach(fn(item) { ... })
"""

import pytest
from silk.interpreter import Interpreter


class TestForEachBuiltin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_foreach_basic(self):
        output = self._run('''
forEach([1, 2, 3], fn(x) { print(x) })
''')
        assert output == ["1", "2", "3"]

    def test_foreach_with_named_fn(self):
        output = self._run('''
fn greet(name) { print(f"Hello {name}") }
forEach(["Alice", "Bob"], greet)
''')
        assert output[0] == "Hello Alice"
        assert output[1] == "Hello Bob"

    def test_foreach_empty_array(self):
        output = self._run('''
forEach([], fn(x) { print(x) })
print("done")
''')
        assert output[-1] == "done"

    def test_foreach_returns_null(self):
        output = self._run('''
let result = forEach([1], fn(x) { print(x) })
print(result)
''')
        assert output[-1] == "null"


class TestForEachMethod:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_foreach_method(self):
        output = self._run('''
[10, 20, 30].forEach(fn(x) { print(x) })
''')
        assert output == ["10", "20", "30"]

    def test_foreach_method_with_side_effect(self):
        output = self._run('''
let mut total = 0
[1, 2, 3, 4].forEach(fn(x) { total += x })
print(total)
''')
        assert output[-1] == "10"

    def test_foreach_method_chain_context(self):
        output = self._run('''
let names = ["alice", "bob"]
names.forEach(fn(name) {
    print(name.upper())
})
''')
        assert output[0] == "ALICE"
        assert output[1] == "BOB"

    def test_foreach_on_hashmap_keys(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
m.keys().forEach(fn(k) { print(k) })
''')
        assert len(output) == 2
