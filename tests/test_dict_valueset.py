"""
Tests for dict .valueSet() method.
"""

from silk.interpreter import Interpreter


class TestDictValueSet:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_valueSet_with_dupes(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 1, "d": 3}
print(d.valueSet())
''')
        assert output[-1] == "[1, 2, 3]"

    def test_valueSet_unique(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.valueSet())
''')
        assert output[-1] == "[1, 2]"
