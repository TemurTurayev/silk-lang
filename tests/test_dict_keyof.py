"""
Tests for dict .keyOf(value) method.
"""

from silk.interpreter import Interpreter


class TestDictKeyOf:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_keyOf_found(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.keyOf(2))
''')
        assert output[-1] == "b"

    def test_keyOf_not_found(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.keyOf(99))
''')
        assert output[-1] == "null"
