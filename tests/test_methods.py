"""
Tests for string and array methods.

String methods: .length, .upper(), .lower(), .strip(), .trim(),
                .replace(), .starts_with(), .ends_with(),
                .contains(), .split(), .chars()
Array methods:  .length, .push(), .pop(), .slice(), .reverse(),
                .map(), .filter(), .join(), .contains(), .indexOf()
"""

import pytest
from silk.interpreter import Interpreter


class TestStringMethods:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_string_length(self):
        output = self._run('print("hello".length)')
        assert output[-1] == "5"

    def test_string_upper(self):
        output = self._run('print("hello".upper())')
        assert output[-1] == "HELLO"

    def test_string_lower(self):
        output = self._run('print("HELLO".lower())')
        assert output[-1] == "hello"

    def test_string_strip(self):
        output = self._run('print("  hello  ".strip())')
        assert output[-1] == "hello"

    def test_string_trim(self):
        """trim() is an alias for strip()."""
        output = self._run('print("  world  ".trim())')
        assert output[-1] == "world"

    def test_string_replace(self):
        output = self._run('print("hello world".replace("world", "silk"))')
        assert output[-1] == "hello silk"

    def test_string_starts_with(self):
        output = self._run('''
print("hello".starts_with("hel"))
print("hello".starts_with("xyz"))
''')
        assert output[0] == "true"
        assert output[1] == "false"

    def test_string_ends_with(self):
        output = self._run('''
print("hello".ends_with("llo"))
print("hello".ends_with("xyz"))
''')
        assert output[0] == "true"
        assert output[1] == "false"

    def test_string_contains(self):
        output = self._run('''
print("hello world".contains("world"))
print("hello world".contains("xyz"))
''')
        assert output[0] == "true"
        assert output[1] == "false"

    def test_string_split(self):
        output = self._run('''
let parts = "a,b,c".split(",")
print(parts)
''')
        assert output[-1] == "[a, b, c]"

    def test_string_split_default(self):
        output = self._run('''
let parts = "hello world".split(" ")
print(parts)
''')
        assert output[-1] == "[hello, world]"

    def test_string_chars(self):
        output = self._run('''
let c = "abc".chars()
print(c)
''')
        assert output[-1] == "[a, b, c]"

    def test_string_index_access(self):
        output = self._run('print("hello"[1])')
        assert output[-1] == "e"

    def test_string_method_chain(self):
        output = self._run('print("  Hello  ".strip().lower())')
        assert output[-1] == "hello"


class TestArrayMethods:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_array_length(self):
        output = self._run('print([1, 2, 3].length)')
        assert output[-1] == "3"

    def test_array_push(self):
        output = self._run('''
let mut arr = [1, 2]
arr.push(3)
print(arr)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_array_pop(self):
        output = self._run('''
let mut arr = [1, 2, 3]
let last = arr.pop()
print(last)
print(arr)
''')
        assert output[0] == "3"
        assert output[1] == "[1, 2]"

    def test_array_slice(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
print(arr.slice(1, 3))
''')
        assert output[-1] == "[2, 3]"

    def test_array_reverse(self):
        output = self._run('''
let arr = [1, 2, 3]
print(arr.reverse())
''')
        assert output[-1] == "[3, 2, 1]"

    def test_array_contains(self):
        output = self._run('''
print([1, 2, 3].contains(2))
print([1, 2, 3].contains(5))
''')
        assert output[0] == "true"
        assert output[1] == "false"

    def test_array_join(self):
        output = self._run('''
print([1, 2, 3].join(", "))
''')
        assert output[-1] == "1, 2, 3"

    def test_array_join_no_sep(self):
        output = self._run('''
print(["a", "b", "c"].join(""))
''')
        assert output[-1] == "abc"

    def test_array_indexOf(self):
        output = self._run('''
print([10, 20, 30].indexOf(20))
print([10, 20, 30].indexOf(99))
''')
        assert output[0] == "1"
        assert output[1] == "-1"

    def test_array_map(self):
        output = self._run('''
let result = [1, 2, 3].map(fn(x) { return x * 2 })
print(result)
''')
        assert output[-1] == "[2, 4, 6]"

    def test_array_filter(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].filter(fn(x) { return x > 3 })
print(result)
''')
        assert output[-1] == "[4, 5]"

    def test_array_method_chain(self):
        output = self._run('''
let result = [3, 1, 2].reverse().join("-")
print(result)
''')
        assert output[-1] == "2-1-3"
