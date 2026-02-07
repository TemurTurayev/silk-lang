"""
Tests for dict .toSortedValues() method.
"""

from silk.interpreter import Interpreter


class TestDictToSortedValues:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSortedValues_basic(self):
        output = self._run('''
let d = {"c": 3, "a": 1, "b": 2}
print(d.toSortedValues())
''')
        assert output[-1] == '[1, 2, 3]'

    def test_toSortedValues_strings(self):
        output = self._run('''
let d = {"x": "banana", "y": "apple"}
print(d.toSortedValues())
''')
        assert output[-1] == '[apple, banana]'
