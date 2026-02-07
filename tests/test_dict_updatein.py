"""
Tests for dict .updateIn(key, fn) method.
"""

from silk.interpreter import Interpreter


class TestDictUpdateIn:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_updateIn_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.updateIn("b", |v| v * 10))
''')
        assert output[-1] == '{"a": 1, "b": 20, "c": 3}'

    def test_updateIn_string(self):
        output = self._run('''
let d = {"name": "alice"}
print(d.updateIn("name", |v| v.toUpper()))
''')
        assert output[-1] == '{"name": ALICE}'
