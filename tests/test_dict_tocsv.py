"""
Tests for dict .toCSV() method.
"""

from silk.interpreter import Interpreter


class TestDictToCSV:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCSV_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30}
print(d.toCSV())
''')
        assert output[-1] == "name,age\nAlice,30"

    def test_toCSV_numbers(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.toCSV())
''')
        assert output[-1] == "a,b\n1,2"
