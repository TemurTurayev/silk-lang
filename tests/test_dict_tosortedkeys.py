"""
Tests for dict .toSortedKeys() method.
"""

from silk.interpreter import Interpreter


class TestDictToSortedKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSortedKeys_basic(self):
        output = self._run('''
let d = {"c": 3, "a": 1, "b": 2}
print(d.toSortedKeys())
''')
        assert output[-1] == '{"a": 1, "b": 2, "c": 3}'

    def test_toSortedKeys_already_sorted(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.toSortedKeys())
''')
        assert output[-1] == '{"a": 1, "b": 2}'
