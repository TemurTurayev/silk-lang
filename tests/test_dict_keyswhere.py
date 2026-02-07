"""
Tests for dict .keysWhere(fn) method.
"""

from silk.interpreter import Interpreter


class TestDictKeysWhere:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_keysWhere_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 5, "c": 3}
print(d.keysWhere(|k, v| v > 2))
''')
        assert output[-1] == '[b, c]'

    def test_keysWhere_none(self):
        output = self._run('''
let d = {"x": 1}
print(d.keysWhere(|k, v| v > 100))
''')
        assert output[-1] == '[]'
