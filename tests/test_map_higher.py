"""
Tests for map .filter() and .map() higher-order methods.
"""

from silk.interpreter import Interpreter


class TestMapFilter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_filter_values(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
let filtered = m.filter(|k, v| v > 1)
print(filtered.length)
''')
        assert output[-1] == "2"

    def test_filter_empty_result(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
let filtered = m.filter(|k, v| v > 10)
print(filtered.length)
''')
        assert output[-1] == "0"


class TestMapMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_map_values(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
let doubled = m.map(|k, v| v * 2)
print(doubled["a"])
print(doubled["b"])
''')
        assert output[-2] == "2"
        assert output[-1] == "4"

    def test_map_keys(self):
        output = self._run('''
let m = {"hello": 1, "world": 2}
let result = m.map(|k, v| v + 10)
print(result["hello"])
''')
        assert output[-1] == "11"
