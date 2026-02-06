"""
Tests for reduce builtin and array method.

Syntax:
  reduce(array, fn(acc, item) { ... }, initial)
  array.reduce(fn(acc, item) { ... }, initial)
"""

import pytest
from silk.interpreter import Interpreter


class TestReduceBuiltin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reduce_sum(self):
        output = self._run('''
let total = reduce([1, 2, 3, 4], fn(acc, x) { return acc + x }, 0)
print(total)
''')
        assert output[-1] == "10"

    def test_reduce_product(self):
        output = self._run('''
let product = reduce([1, 2, 3, 4], fn(acc, x) { return acc * x }, 1)
print(product)
''')
        assert output[-1] == "24"

    def test_reduce_string_concat(self):
        output = self._run('''
let result = reduce(["a", "b", "c"], fn(acc, s) { return acc + s }, "")
print(result)
''')
        assert output[-1] == "abc"

    def test_reduce_with_named_fn(self):
        output = self._run('''
fn add(a, b) { return a + b }
print(reduce([10, 20, 30], add, 0))
''')
        assert output[-1] == "60"

    def test_reduce_empty_array(self):
        output = self._run('''
print(reduce([], fn(acc, x) { return acc + x }, 42))
''')
        assert output[-1] == "42"


class TestReduceMethod:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reduce_method_sum(self):
        output = self._run('''
let total = [1, 2, 3].reduce(fn(acc, x) { return acc + x }, 0)
print(total)
''')
        assert output[-1] == "6"

    def test_reduce_method_max(self):
        output = self._run('''
let nums = [3, 7, 2, 9, 1]
let biggest = nums.reduce(fn(max, x) {
    return if x > max then x else max
}, 0)
print(biggest)
''')
        assert output[-1] == "9"

    def test_reduce_method_count(self):
        output = self._run('''
let count = [true, false, true, true].reduce(fn(n, x) {
    return if x then n + 1 else n
}, 0)
print(count)
''')
        assert output[-1] == "3"

    def test_reduce_build_hashmap(self):
        output = self._run('''
let words = ["apple", "banana", "cherry"]
let lengths = words.reduce(fn(m, w) {
    m[w] = len(w)
    return m
}, {:})
print(lengths["banana"])
''')
        assert output[-1] == "6"
