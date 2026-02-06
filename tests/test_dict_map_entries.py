"""
Tests for dict .mapEntries() method.
"""

from silk.interpreter import Interpreter


class TestDictMapEntries:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapEntries_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
let result = d.mapEntries(|k, v| [k.toUpper(), v * 10])
print(result.get("A"))
print(result.get("B"))
''')
        assert output[-2] == "10"
        assert output[-1] == "20"

    def test_mapEntries_swap(self):
        output = self._run('''
let d = {"x": 1}
let result = d.mapEntries(|k, v| [v, k])
print(result.get(1))
''')
        assert output[-1] == "x"

    def test_mapEntries_length(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
let result = d.mapEntries(|k, v| [k, v + 1])
print(result.length)
''')
        assert output[-1] == "3"
