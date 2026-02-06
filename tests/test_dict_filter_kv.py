"""
Tests for dict .filterKeys() and .filterValues() methods.
"""

from silk.interpreter import Interpreter


class TestDictFilterKV:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_filterValues_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 5, "c": 3}
let result = d.filterValues(|v| v > 2)
print(result.length)
print(result.get("b"))
''')
        assert output[-2] == "2"
        assert output[-1] == "5"

    def test_filterKeys_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30, "city": "NYC"}
let result = d.filterKeys(|k| k.length > 3)
print(result.length)
print(result.get("name"))
print(result.get("city"))
''')
        assert output[-3] == "2"
        assert output[-2] == "Alice"
        assert output[-1] == "NYC"

    def test_filterValues_empty_result(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
let result = d.filterValues(|v| v > 10)
print(result.length)
''')
        assert output[-1] == "0"
