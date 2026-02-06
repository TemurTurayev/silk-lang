"""
Tests for dict .toArray() and .mapValues() methods.
"""

from silk.interpreter import Interpreter


class TestDictTransform:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toArray(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
let arr = m.toArray()
print(arr.length)
''')
        assert output[-1] == "2"

    def test_mapValues(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
let doubled = m.mapValues(|v| v * 2)
print(doubled.get("a"))
print(doubled.get("b"))
''')
        assert output[-2] == "2"
        assert output[-1] == "4"

    def test_mapValues_to_string(self):
        output = self._run('''
let scores = {"math": 90, "sci": 85}
let grades = scores.mapValues(|v| if v >= 90 then "A" else "B")
print(grades.get("math"))
print(grades.get("sci"))
''')
        assert output[-2] == "A"
        assert output[-1] == "B"

    def test_toArray_entries_format(self):
        """toArray returns [key, value] pairs like entries()."""
        output = self._run('''
let m = {"x": 10}
let arr = m.toArray()
print(arr[0][0])
print(arr[0][1])
''')
        assert output[-2] == "x"
        assert output[-1] == "10"
