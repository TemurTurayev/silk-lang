"""
Tests for dict .sortByKey() method.
"""

from silk.interpreter import Interpreter


class TestDictSortByKey:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sortByKey_basic(self):
        output = self._run('''
let d = {"c": 3, "a": 1, "b": 2}
print(d.sortByKey())
''')
        assert output[-1] == '{"a": 1, "b": 2, "c": 3}'

    def test_sortByKey_numbers(self):
        output = self._run('''
let d = {"z": 1, "m": 2}
print(d.sortByKey())
''')
        assert output[-1] == '{"m": 2, "z": 1}'
