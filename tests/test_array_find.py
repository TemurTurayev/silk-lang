"""
Tests for array .find() and .findIndex() methods.
"""

from silk.interpreter import Interpreter


class TestArrayFind:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_find_number(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
let result = arr.find(fn(x) { return x > 3 })
print(result)
''')
        assert output[-1] == "4"

    def test_find_no_match(self):
        output = self._run('''
let arr = [1, 2, 3]
let result = arr.find(fn(x) { return x > 10 })
print(result)
''')
        assert output[-1] == "null"

    def test_find_string(self):
        output = self._run('''
let names = ["alice", "bob", "charlie"]
let result = names.find(fn(n) { return n.starts_with("b") })
print(result)
''')
        assert output[-1] == "bob"

    def test_find_first_match(self):
        output = self._run('''
let arr = [10, 20, 30, 40]
let result = arr.find(fn(x) { return x >= 20 })
print(result)
''')
        assert output[-1] == "20"

    def test_findIndex_found(self):
        output = self._run('''
let arr = [10, 20, 30, 40]
let idx = arr.findIndex(fn(x) { return x == 30 })
print(idx)
''')
        assert output[-1] == "2"

    def test_findIndex_not_found(self):
        output = self._run('''
let arr = [1, 2, 3]
let idx = arr.findIndex(fn(x) { return x == 99 })
print(idx)
''')
        assert output[-1] == "-1"

    def test_findIndex_first_match(self):
        output = self._run('''
let arr = [5, 10, 15, 20]
let idx = arr.findIndex(fn(x) { return x > 8 })
print(idx)
''')
        assert output[-1] == "1"

    def test_find_empty_array(self):
        output = self._run('''
let arr = []
let result = arr.find(fn(x) { return x > 0 })
print(result)
''')
        assert output[-1] == "null"

    def test_findIndex_empty_array(self):
        output = self._run('''
let arr = []
let idx = arr.findIndex(fn(x) { return x > 0 })
print(idx)
''')
        assert output[-1] == "-1"
